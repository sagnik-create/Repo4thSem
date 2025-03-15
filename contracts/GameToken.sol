// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract GameToken {
    address public owner;
    mapping(address => uint256) public balances;

    event CoinsReceived(address indexed player, uint256 amount);
    event CertificatePurchased(address indexed player, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    function receiveCoins(address player, uint256 amount) public {
        require(msg.sender == owner, "Only owner can add coins");
        balances[player] += amount;
        emit CoinsReceived(player, amount);
    }

    function buyCertificate(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Not enough coins");
        balances[msg.sender] -= amount;
        emit CertificatePurchased(msg.sender, amount);
    }

    function getBalance(address player) public view returns (uint256) {
        return balances[player];
    }
}
