from web3.auto import Web3
from web3.middleware import geth_poa_middleware
import json
import ruamel.yaml as yaml
import sys

w3 = Web3(Web3.HTTPProvider("https://rpc.goerli.mudit.blog"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

testnet_config_path = "genesis-config.yaml"
if len(sys.argv) > 1:
    testnet_config_path = sys.argv[1]

with open(testnet_config_path) as stream:
    data = yaml.safe_load(stream)

out = {
    "config": {
        "chainId": int(data['chain_id']),
        "homesteadBlock": 0,
        "daoForkSupport": True,
        "eip150Block": 0,
        "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "eip155Block": 0,
        "eip158Block": 0,
        "byzantiumBlock": 0,
        "constantinopleBlock": 0,
        "petersburgBlock": 0,
        "istanbulBlock": 1561651,
        "berlinBlock": 4460644,
        "londonBlock": 5062605,
        "mergeForkBlock": w3.eth.block_number + 800,
        "terminalTotalDifficulty": w3.eth.get_block('latest')['totalDifficulty'] + 1400,
        "clique": { "period": 15, "epoch": 30000 },
        "trustedCheckpoint": {
            "sectionIndex": 66,
            "sectionHead": "0xeea3a7b2cb275956f3049dd27e6cdacd8a6ef86738d593d556efee5361019475",
            "chtRoot": "0x11712af50b4083dc5910e452ca69fbfc0f2940770b9846200a573f87a0af94e6",
            "bloomRoot": "0x331b7a7b273e81daeac8cafb9952a16669d7facc7be3b0ebd3a792b4d8b95cc5"
        },
        "trustedCheckpointOracle": {
            "address": "0x18ca0e045f0d772a851bc7e48357bcaab0a0795d",
            "signers": [
                "0x4769bcad07e3b938b7f43eb7d278bc7cb9effb38",
                "0x78d1ad571a1a09d60d9bbf25894b44e4c8859595",
                "0x286834935f4a8cfb4ff4c77d5770c2775ae2b0e7",
                "0xb86e2b0ab5a4b1373e40c51a7c712c70ba2f9f8e",
                "0x0df8fa387c602ae62559cc4afa4972a7045d6707"
            ],
            "threshold": 2
        }
    },
    "nonce": "0x0",
    "timestamp": "0x5c51a607",
    "extraData": "0x22466c6578692069732061207468696e6722202d204166726900000000000000e0a2bd4258d2768837baa26a28fe71dc079f84c70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "gasLimit": "0xa00000",
    "difficulty": "0x1",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "coinbase": "0x0000000000000000000000000000000000000000",
    "alloc": {
        "0000000000000000000000000000000000000000": { "balance": "0x1" },
        "0000000000000000000000000000000000000001": { "balance": "0x1" },
        "0000000000000000000000000000000000000002": { "balance": "0x1" },
        "0000000000000000000000000000000000000003": { "balance": "0x1" },
        "0000000000000000000000000000000000000004": { "balance": "0x1" },
        "0000000000000000000000000000000000000005": { "balance": "0x1" },
        "0000000000000000000000000000000000000006": { "balance": "0x1" },
        "0000000000000000000000000000000000000007": { "balance": "0x1" },
        "0000000000000000000000000000000000000008": { "balance": "0x1" },
        "0000000000000000000000000000000000000009": { "balance": "0x1" },
        "000000000000000000000000000000000000000a": { "balance": "0x1" },
        "000000000000000000000000000000000000000b": { "balance": "0x1" },
        "000000000000000000000000000000000000000c": { "balance": "0x1" },
        "000000000000000000000000000000000000000d": { "balance": "0x1" },
        "000000000000000000000000000000000000000e": { "balance": "0x1" },
        "000000000000000000000000000000000000000f": { "balance": "0x1" },
        "0000000000000000000000000000000000000010": { "balance": "0x1" },
        "0000000000000000000000000000000000000011": { "balance": "0x1" },
        "0000000000000000000000000000000000000012": { "balance": "0x1" },
        "0000000000000000000000000000000000000013": { "balance": "0x1" },
        "0000000000000000000000000000000000000014": { "balance": "0x1" },
        "0000000000000000000000000000000000000015": { "balance": "0x1" },
        "0000000000000000000000000000000000000016": { "balance": "0x1" },
        "0000000000000000000000000000000000000017": { "balance": "0x1" },
        "0000000000000000000000000000000000000018": { "balance": "0x1" },
        "0000000000000000000000000000000000000019": { "balance": "0x1" },
        "000000000000000000000000000000000000001a": { "balance": "0x1" },
        "000000000000000000000000000000000000001b": { "balance": "0x1" },
        "000000000000000000000000000000000000001c": { "balance": "0x1" },
        "000000000000000000000000000000000000001d": { "balance": "0x1" },
        "000000000000000000000000000000000000001e": { "balance": "0x1" },
        "000000000000000000000000000000000000001f": { "balance": "0x1" },
        "0000000000000000000000000000000000000020": { "balance": "0x1" },
        "0000000000000000000000000000000000000021": { "balance": "0x1" },
        "0000000000000000000000000000000000000022": { "balance": "0x1" },
        "0000000000000000000000000000000000000023": { "balance": "0x1" },
        "0000000000000000000000000000000000000024": { "balance": "0x1" },
        "0000000000000000000000000000000000000025": { "balance": "0x1" },
        "0000000000000000000000000000000000000026": { "balance": "0x1" },
        "0000000000000000000000000000000000000027": { "balance": "0x1" },
        "0000000000000000000000000000000000000028": { "balance": "0x1" },
        "0000000000000000000000000000000000000029": { "balance": "0x1" },
        "000000000000000000000000000000000000002a": { "balance": "0x1" },
        "000000000000000000000000000000000000002b": { "balance": "0x1" },
        "000000000000000000000000000000000000002c": { "balance": "0x1" },
        "000000000000000000000000000000000000002d": { "balance": "0x1" },
        "000000000000000000000000000000000000002e": { "balance": "0x1" },
        "000000000000000000000000000000000000002f": { "balance": "0x1" },
        "0000000000000000000000000000000000000030": { "balance": "0x1" },
        "0000000000000000000000000000000000000031": { "balance": "0x1" },
        "0000000000000000000000000000000000000032": { "balance": "0x1" },
        "0000000000000000000000000000000000000033": { "balance": "0x1" },
        "0000000000000000000000000000000000000034": { "balance": "0x1" },
        "0000000000000000000000000000000000000035": { "balance": "0x1" },
        "0000000000000000000000000000000000000036": { "balance": "0x1" },
        "0000000000000000000000000000000000000037": { "balance": "0x1" },
        "0000000000000000000000000000000000000038": { "balance": "0x1" },
        "0000000000000000000000000000000000000039": { "balance": "0x1" },
        "000000000000000000000000000000000000003a": { "balance": "0x1" },
        "000000000000000000000000000000000000003b": { "balance": "0x1" },
        "000000000000000000000000000000000000003c": { "balance": "0x1" },
        "000000000000000000000000000000000000003d": { "balance": "0x1" },
        "000000000000000000000000000000000000003e": { "balance": "0x1" },
        "000000000000000000000000000000000000003f": { "balance": "0x1" },
        "0000000000000000000000000000000000000040": { "balance": "0x1" },
        "0000000000000000000000000000000000000041": { "balance": "0x1" },
        "0000000000000000000000000000000000000042": { "balance": "0x1" },
        "0000000000000000000000000000000000000043": { "balance": "0x1" },
        "0000000000000000000000000000000000000044": { "balance": "0x1" },
        "0000000000000000000000000000000000000045": { "balance": "0x1" },
        "0000000000000000000000000000000000000046": { "balance": "0x1" },
        "0000000000000000000000000000000000000047": { "balance": "0x1" },
        "0000000000000000000000000000000000000048": { "balance": "0x1" },
        "0000000000000000000000000000000000000049": { "balance": "0x1" },
        "000000000000000000000000000000000000004a": { "balance": "0x1" },
        "000000000000000000000000000000000000004b": { "balance": "0x1" },
        "000000000000000000000000000000000000004c": { "balance": "0x1" },
        "000000000000000000000000000000000000004d": { "balance": "0x1" },
        "000000000000000000000000000000000000004e": { "balance": "0x1" },
        "000000000000000000000000000000000000004f": { "balance": "0x1" },
        "0000000000000000000000000000000000000050": { "balance": "0x1" },
        "0000000000000000000000000000000000000051": { "balance": "0x1" },
        "0000000000000000000000000000000000000052": { "balance": "0x1" },
        "0000000000000000000000000000000000000053": { "balance": "0x1" },
        "0000000000000000000000000000000000000054": { "balance": "0x1" },
        "0000000000000000000000000000000000000055": { "balance": "0x1" },
        "0000000000000000000000000000000000000056": { "balance": "0x1" },
        "0000000000000000000000000000000000000057": { "balance": "0x1" },
        "0000000000000000000000000000000000000058": { "balance": "0x1" },
        "0000000000000000000000000000000000000059": { "balance": "0x1" },
        "000000000000000000000000000000000000005a": { "balance": "0x1" },
        "000000000000000000000000000000000000005b": { "balance": "0x1" },
        "000000000000000000000000000000000000005c": { "balance": "0x1" },
        "000000000000000000000000000000000000005d": { "balance": "0x1" },
        "000000000000000000000000000000000000005e": { "balance": "0x1" },
        "000000000000000000000000000000000000005f": { "balance": "0x1" },
        "0000000000000000000000000000000000000060": { "balance": "0x1" },
        "0000000000000000000000000000000000000061": { "balance": "0x1" },
        "0000000000000000000000000000000000000062": { "balance": "0x1" },
        "0000000000000000000000000000000000000063": { "balance": "0x1" },
        "0000000000000000000000000000000000000064": { "balance": "0x1" },
        "0000000000000000000000000000000000000065": { "balance": "0x1" },
        "0000000000000000000000000000000000000066": { "balance": "0x1" },
        "0000000000000000000000000000000000000067": { "balance": "0x1" },
        "0000000000000000000000000000000000000068": { "balance": "0x1" },
        "0000000000000000000000000000000000000069": { "balance": "0x1" },
        "000000000000000000000000000000000000006a": { "balance": "0x1" },
        "000000000000000000000000000000000000006b": { "balance": "0x1" },
        "000000000000000000000000000000000000006c": { "balance": "0x1" },
        "000000000000000000000000000000000000006d": { "balance": "0x1" },
        "000000000000000000000000000000000000006e": { "balance": "0x1" },
        "000000000000000000000000000000000000006f": { "balance": "0x1" },
        "0000000000000000000000000000000000000070": { "balance": "0x1" },
        "0000000000000000000000000000000000000071": { "balance": "0x1" },
        "0000000000000000000000000000000000000072": { "balance": "0x1" },
        "0000000000000000000000000000000000000073": { "balance": "0x1" },
        "0000000000000000000000000000000000000074": { "balance": "0x1" },
        "0000000000000000000000000000000000000075": { "balance": "0x1" },
        "0000000000000000000000000000000000000076": { "balance": "0x1" },
        "0000000000000000000000000000000000000077": { "balance": "0x1" },
        "0000000000000000000000000000000000000078": { "balance": "0x1" },
        "0000000000000000000000000000000000000079": { "balance": "0x1" },
        "000000000000000000000000000000000000007a": { "balance": "0x1" },
        "000000000000000000000000000000000000007b": { "balance": "0x1" },
        "000000000000000000000000000000000000007c": { "balance": "0x1" },
        "000000000000000000000000000000000000007d": { "balance": "0x1" },
        "000000000000000000000000000000000000007e": { "balance": "0x1" },
        "000000000000000000000000000000000000007f": { "balance": "0x1" },
        "0000000000000000000000000000000000000080": { "balance": "0x1" },
        "0000000000000000000000000000000000000081": { "balance": "0x1" },
        "0000000000000000000000000000000000000082": { "balance": "0x1" },
        "0000000000000000000000000000000000000083": { "balance": "0x1" },
        "0000000000000000000000000000000000000084": { "balance": "0x1" },
        "0000000000000000000000000000000000000085": { "balance": "0x1" },
        "0000000000000000000000000000000000000086": { "balance": "0x1" },
        "0000000000000000000000000000000000000087": { "balance": "0x1" },
        "0000000000000000000000000000000000000088": { "balance": "0x1" },
        "0000000000000000000000000000000000000089": { "balance": "0x1" },
        "000000000000000000000000000000000000008a": { "balance": "0x1" },
        "000000000000000000000000000000000000008b": { "balance": "0x1" },
        "000000000000000000000000000000000000008c": { "balance": "0x1" },
        "000000000000000000000000000000000000008d": { "balance": "0x1" },
        "000000000000000000000000000000000000008e": { "balance": "0x1" },
        "000000000000000000000000000000000000008f": { "balance": "0x1" },
        "0000000000000000000000000000000000000090": { "balance": "0x1" },
        "0000000000000000000000000000000000000091": { "balance": "0x1" },
        "0000000000000000000000000000000000000092": { "balance": "0x1" },
        "0000000000000000000000000000000000000093": { "balance": "0x1" },
        "0000000000000000000000000000000000000094": { "balance": "0x1" },
        "0000000000000000000000000000000000000095": { "balance": "0x1" },
        "0000000000000000000000000000000000000096": { "balance": "0x1" },
        "0000000000000000000000000000000000000097": { "balance": "0x1" },
        "0000000000000000000000000000000000000098": { "balance": "0x1" },
        "0000000000000000000000000000000000000099": { "balance": "0x1" },
        "000000000000000000000000000000000000009a": { "balance": "0x1" },
        "000000000000000000000000000000000000009b": { "balance": "0x1" },
        "000000000000000000000000000000000000009c": { "balance": "0x1" },
        "000000000000000000000000000000000000009d": { "balance": "0x1" },
        "000000000000000000000000000000000000009e": { "balance": "0x1" },
        "000000000000000000000000000000000000009f": { "balance": "0x1" },
        "00000000000000000000000000000000000000a0": { "balance": "0x1" },
        "00000000000000000000000000000000000000a1": { "balance": "0x1" },
        "00000000000000000000000000000000000000a2": { "balance": "0x1" },
        "00000000000000000000000000000000000000a3": { "balance": "0x1" },
        "00000000000000000000000000000000000000a4": { "balance": "0x1" },
        "00000000000000000000000000000000000000a5": { "balance": "0x1" },
        "00000000000000000000000000000000000000a6": { "balance": "0x1" },
        "00000000000000000000000000000000000000a7": { "balance": "0x1" },
        "00000000000000000000000000000000000000a8": { "balance": "0x1" },
        "00000000000000000000000000000000000000a9": { "balance": "0x1" },
        "00000000000000000000000000000000000000aa": { "balance": "0x1" },
        "00000000000000000000000000000000000000ab": { "balance": "0x1" },
        "00000000000000000000000000000000000000ac": { "balance": "0x1" },
        "00000000000000000000000000000000000000ad": { "balance": "0x1" },
        "00000000000000000000000000000000000000ae": { "balance": "0x1" },
        "00000000000000000000000000000000000000af": { "balance": "0x1" },
        "00000000000000000000000000000000000000b0": { "balance": "0x1" },
        "00000000000000000000000000000000000000b1": { "balance": "0x1" },
        "00000000000000000000000000000000000000b2": { "balance": "0x1" },
        "00000000000000000000000000000000000000b3": { "balance": "0x1" },
        "00000000000000000000000000000000000000b4": { "balance": "0x1" },
        "00000000000000000000000000000000000000b5": { "balance": "0x1" },
        "00000000000000000000000000000000000000b6": { "balance": "0x1" },
        "00000000000000000000000000000000000000b7": { "balance": "0x1" },
        "00000000000000000000000000000000000000b8": { "balance": "0x1" },
        "00000000000000000000000000000000000000b9": { "balance": "0x1" },
        "00000000000000000000000000000000000000ba": { "balance": "0x1" },
        "00000000000000000000000000000000000000bb": { "balance": "0x1" },
        "00000000000000000000000000000000000000bc": { "balance": "0x1" },
        "00000000000000000000000000000000000000bd": { "balance": "0x1" },
        "00000000000000000000000000000000000000be": { "balance": "0x1" },
        "00000000000000000000000000000000000000bf": { "balance": "0x1" },
        "00000000000000000000000000000000000000c0": { "balance": "0x1" },
        "00000000000000000000000000000000000000c1": { "balance": "0x1" },
        "00000000000000000000000000000000000000c2": { "balance": "0x1" },
        "00000000000000000000000000000000000000c3": { "balance": "0x1" },
        "00000000000000000000000000000000000000c4": { "balance": "0x1" },
        "00000000000000000000000000000000000000c5": { "balance": "0x1" },
        "00000000000000000000000000000000000000c6": { "balance": "0x1" },
        "00000000000000000000000000000000000000c7": { "balance": "0x1" },
        "00000000000000000000000000000000000000c8": { "balance": "0x1" },
        "00000000000000000000000000000000000000c9": { "balance": "0x1" },
        "00000000000000000000000000000000000000ca": { "balance": "0x1" },
        "00000000000000000000000000000000000000cb": { "balance": "0x1" },
        "00000000000000000000000000000000000000cc": { "balance": "0x1" },
        "00000000000000000000000000000000000000cd": { "balance": "0x1" },
        "00000000000000000000000000000000000000ce": { "balance": "0x1" },
        "00000000000000000000000000000000000000cf": { "balance": "0x1" },
        "00000000000000000000000000000000000000d0": { "balance": "0x1" },
        "00000000000000000000000000000000000000d1": { "balance": "0x1" },
        "00000000000000000000000000000000000000d2": { "balance": "0x1" },
        "00000000000000000000000000000000000000d3": { "balance": "0x1" },
        "00000000000000000000000000000000000000d4": { "balance": "0x1" },
        "00000000000000000000000000000000000000d5": { "balance": "0x1" },
        "00000000000000000000000000000000000000d6": { "balance": "0x1" },
        "00000000000000000000000000000000000000d7": { "balance": "0x1" },
        "00000000000000000000000000000000000000d8": { "balance": "0x1" },
        "00000000000000000000000000000000000000d9": { "balance": "0x1" },
        "00000000000000000000000000000000000000da": { "balance": "0x1" },
        "00000000000000000000000000000000000000db": { "balance": "0x1" },
        "00000000000000000000000000000000000000dc": { "balance": "0x1" },
        "00000000000000000000000000000000000000dd": { "balance": "0x1" },
        "00000000000000000000000000000000000000de": { "balance": "0x1" },
        "00000000000000000000000000000000000000df": { "balance": "0x1" },
        "00000000000000000000000000000000000000e0": { "balance": "0x1" },
        "00000000000000000000000000000000000000e1": { "balance": "0x1" },
        "00000000000000000000000000000000000000e2": { "balance": "0x1" },
        "00000000000000000000000000000000000000e3": { "balance": "0x1" },
        "00000000000000000000000000000000000000e4": { "balance": "0x1" },
        "00000000000000000000000000000000000000e5": { "balance": "0x1" },
        "00000000000000000000000000000000000000e6": { "balance": "0x1" },
        "00000000000000000000000000000000000000e7": { "balance": "0x1" },
        "00000000000000000000000000000000000000e8": { "balance": "0x1" },
        "00000000000000000000000000000000000000e9": { "balance": "0x1" },
        "00000000000000000000000000000000000000ea": { "balance": "0x1" },
        "00000000000000000000000000000000000000eb": { "balance": "0x1" },
        "00000000000000000000000000000000000000ec": { "balance": "0x1" },
        "00000000000000000000000000000000000000ed": { "balance": "0x1" },
        "00000000000000000000000000000000000000ee": { "balance": "0x1" },
        "00000000000000000000000000000000000000ef": { "balance": "0x1" },
        "00000000000000000000000000000000000000f0": { "balance": "0x1" },
        "00000000000000000000000000000000000000f1": { "balance": "0x1" },
        "00000000000000000000000000000000000000f2": { "balance": "0x1" },
        "00000000000000000000000000000000000000f3": { "balance": "0x1" },
        "00000000000000000000000000000000000000f4": { "balance": "0x1" },
        "00000000000000000000000000000000000000f5": { "balance": "0x1" },
        "00000000000000000000000000000000000000f6": { "balance": "0x1" },
        "00000000000000000000000000000000000000f7": { "balance": "0x1" },
        "00000000000000000000000000000000000000f8": { "balance": "0x1" },
        "00000000000000000000000000000000000000f9": { "balance": "0x1" },
        "00000000000000000000000000000000000000fa": { "balance": "0x1" },
        "00000000000000000000000000000000000000fb": { "balance": "0x1" },
        "00000000000000000000000000000000000000fc": { "balance": "0x1" },
        "00000000000000000000000000000000000000fd": { "balance": "0x1" },
        "00000000000000000000000000000000000000fe": { "balance": "0x1" },
        "00000000000000000000000000000000000000ff": { "balance": "0x1" },
        "4c2ae482593505f0163cdefc073e81c63cda4107": {
            "balance": "0x152d02c7e14af6800000"
        },
        "a8e8f14732658e4b51e8711931053a8a69baf2b1": {
            "balance": "0x152d02c7e14af6800000"
        },
        "d9a5179f091d85051d3c982785efd1455cec8699": {
            "balance": "0x84595161401484a000000"
        },
        "e0a2bd4258d2768837baa26a28fe71dc079f84c7": {
            "balance": "0x4a47e3c12448f4ad000000"
        }
    },
    "number": "0x0",
    "gasUsed": "0x0",
    "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
}



print(json.dumps(out, indent='  '))
