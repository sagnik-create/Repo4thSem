import solcx
import json

# Install Solidity compiler
solcx.install_solc("0.8.20")

# Compile the contract
compiled_sol = solcx.compile_files(
    ["GameToken.sol"], output_values=["abi", "bin"], solc_version="0.8.20"
)

# Get contract ABI and Bytecode
contract_data = compiled_sol["GameToken.sol:GameToken"]
abi = contract_data["abi"]
bytecode = contract_data["bin"]

# Save ABI & Bytecode to JSON
with open("GameToken.json", "w") as f:
    json.dump({"abi": abi, "bytecode": bytecode}, f)

print("Contract compiled successfully!")
