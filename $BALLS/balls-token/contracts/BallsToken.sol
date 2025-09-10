// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BallsToken is ERC20, Ownable {
    uint256 public constant INITIAL_SUPPLY = 4_000_000_000 * 1e18;
    
    constructor() ERC20("$BALLS", "BALLS") Ownable(msg.sender) {
        _mint(msg.sender, INITIAL_SUPPLY); // 4 billion tokens
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
} 