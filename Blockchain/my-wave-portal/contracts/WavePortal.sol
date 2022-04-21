// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.4;

import "hardhat/console.sol";
// Address : 0x14a5d8b2C5D56F77A7ea2E8Aef5A890DCF932A7f 
contract WavePortal {
    uint256 totalWaves;
    mapping(address => uint32) public waveByPerson;


    function wave() public {
        totalWaves += 1;
        console.log("%s has waved", msg.sender);
        waveByPerson[msg.sender] += 1;
    }

    function getTotalWaves() public view returns (uint256){
        console.log("We have %d total waves!", totalWaves);
        return totalWaves;
    }

    function returnWaveCount() public view returns (uint32) {
        return waveByPerson[msg.sender];
    }
}
