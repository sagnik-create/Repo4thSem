from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

# Load compiled contract ABI & Bytecode
with open("GameToken.json", "r") as f:
    contract_json = json.load(f)
    abi = contract_json["abi"]
    bytecode = contract_json["bytecode"]

# Deploy contract
GameToken = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = GameToken.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress
print(f"Contract deployed at: {contract_address}")

# Save contract address for later use
with open("contract_address.txt", "w") as f:
    f.write(contract_address)
