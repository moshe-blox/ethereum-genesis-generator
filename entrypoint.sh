#!/bin/bash -e
source /config/values.env
SERVER_PORT="${SERVER_PORT:-8000}"

gen_jwt_secret(){
    set -x
    if ! [ -f "/data/el/jwtsecret" ] || [ -f "/data/cl/jwtsecret" ]; then
        mkdir -p /data/el
        echo -n 0x$(openssl rand -hex 32 | tr -d "\n") > /data/el/jwtsecret
        cp /data/el/jwtsecret /data/cl/jwtsecret
    else
        echo "JWT secret already exists. skipping generation..."
    fi
}

gen_el_config(){
    set -x
    if ! [ -f "/data/custom_config_data/geth.json" ]; then
        tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
        mkdir -p /data/custom_config_data
        envsubst < /config/el/genesis-config.yaml > $tmp_dir/genesis-config.yaml
        python3 /apps/el-gen/genesis_geth.py $tmp_dir/genesis-config.yaml      > /data/custom_config_data/geth.json
        python3 /apps/el-gen/genesis_chainspec.py $tmp_dir/genesis-config.yaml > /data/custom_config_data/chainspec.json
        python3 /apps/el-gen/genesis_besu.py $tmp_dir/genesis-config.yaml > /data/custom_config_data/besu.json
    else
        echo "el genesis already exists. skipping generation..."
    fi
}

gen_cl_config(){
    set -x
    # Consensus layer: Check if genesis already exists
    if ! [ -f "/data/custom_config_data/genesis.ssz" ]; then
        tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
        mkdir -p /data/custom_config_data
        # Replace environment vars in files
        envsubst < /config/cl/config.yaml > /data/custom_config_data/config.yaml
        envsubst < /config/cl/mnemonics.yaml > $tmp_dir/mnemonics.yaml
        cp $tmp_dir/mnemonics.yaml /data/custom_config_data/mnemonics.yaml
        # Replace MIN_GENESIS_TIME on config
        sed "s/^MIN_GENESIS_TIME:.*/MIN_GENESIS_TIME: ${GENESIS_TIMESTAMP}/" /data/custom_config_data/config.yaml > /tmp/config.yaml
        mv /tmp/config.yaml /data/custom_config_data/config.yaml
        # Create deposit_contract.txt and deploy_block.txt
        grep DEPOSIT_CONTRACT_ADDRESS /data/custom_config_data/config.yaml | cut -d " " -f2 > /data/custom_config_data/deposit_contract.txt
        echo $DEPOSIT_CONTRACT_BLOCK > /data/custom_config_data/deploy_block.txt
        echo $CL_EXEC_BLOCK > /data/custom_config_data/deposit_contract_block.txt
        echo $BEACON_STATIC_ENR > /data/custom_config_data/bootstrap_nodes.txt
        echo "- $BEACON_STATIC_ENR" > /data/custom_config_data/boot_enr.txt
        # Envsubst mnemonics
        envsubst < /config/cl/mnemonics.yaml > $tmp_dir/mnemonics.yaml
        # Generate genesis
        /usr/local/bin/eth2-testnet-genesis merge \
        --config /data/custom_config_data/config.yaml \
        --mnemonics $tmp_dir/mnemonics.yaml \
        --eth1-config /data/custom_config_data/geth.json \
        --tranches-dir /data/custom_config_data/tranches \
        --state-output /data/custom_config_data/genesis.ssz
    else
        echo "cl genesis already exists. skipping generation..."
    fi
}

gen_all_config(){
    gen_el_config
    gen_cl_config
    gen_jwt_secret
}

case $1 in
  el)
    gen_el_config
    ;;
  cl)
    gen_cl_config
    ;;
  all)
    gen_all_config
    ;;
  *)
    set +x
    echo "Usage: [all|cl|el]"
    exit 1
    ;;
esac

# Start webserver
cd /data && exec python -m SimpleHTTPServer "$SERVER_PORT"
