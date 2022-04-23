// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.4;

import "hardhat/console.sol";

// Address : 0x14a5d8b2C5D56F77A7ea2E8Aef5A890DCF932A7f 

contract WavePortal {
    uint256 totalWaves;

    constructor() payable {
        console.log("We have been constructed!");
    }

    event NewWave(address indexed from, uint256 timestamp, string message);


// Struct is a custom data type, where one can define what should be saved
    struct Wave {
        address waver; //address of the user who waved
        string message; // message as string type
        uint256 timestamp; //timestamp of the wave
    }

// Declaration of the array of structs, to save all the waves
    Wave[] waves;

    function wave(string memory _message) public {
        totalWaves += 1;
        console.log("%s has waved", msg.sender, _message);

// Storing the wave to the "all-waves" array
        waves.push(Wave(msg.sender, _message, block.timestamp));

        emit NewWave(msg.sender, block.timestamp, _message);

        uint256 prizeAmount = 0.0001 ether;
// Checking if Contract has enough ether        
        require(
            prizeAmount <= address(this).balance,
            "sorry, no money left :("
        );
        (bool success, ) = (msg.sender).call{value: prizeAmount}("");
        require(success, "Failed to withdraw!");
    }

// With this func it will be easier to retrieve waves 
    function getAllWaves() public view returns (Wave[] memory){
        return waves;
    }

    function getTotalWaves() public view returns (uint256){
        console.log("We have %d total waves!", totalWaves);
        return totalWaves;
    }
}
