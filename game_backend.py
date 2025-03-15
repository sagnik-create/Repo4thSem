from web3 import Web3
import json
import ipfshttpclient

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

# Load contract ABI
with open('build/contracts/GameToken.json', 'r') as abi_file:
    contract_json = json.load(abi_file)
    contract_abi = contract_json['abi']

contract_address = "0xYourDeployedContractAddress"
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Connect to IPFS
ipfs_client = ipfshttpclient.connect()

# Function to send game coins to blockchain
def send_coins(player_address, amount):
    tx = contract.functions.receiveCoins(player_address, amount).transact()
    web3.eth.wait_for_transaction_receipt(tx)
    print(f"Sent {amount} coins to {player_address}")

# Function to buy a certificate
def buy_certificate(player_address, amount):
    tx = contract.functions.buyCertificate(amount).transact({'from': player_address})
    web3.eth.wait_for_transaction_receipt(tx)
    print(f"Certificate bought for {amount} coins")

# Function to upload certificate to IPFS
def upload_certificate(file_path):
    res = ipfs_client.add(file_path)
    print(f"Certificate stored on IPFS: {res['Hash']}")
    return res['Hash']

# Example Usage
if __name__ == "__main__":
    player_address = web3.eth.accounts[1]
    send_coins(player_address, 100)
    buy_certificate(player_address, 50)
