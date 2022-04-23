const main = async () => {
    const waveContractFactory = await hre.ethers.getContractFactory("WavePortal");
    const waveContract = await waveContractFactory.deploy({
        value: hre.ethers.utils.parseEther("0.1"),
    });
    await waveContract.deployed();
    console.log("Contract Anton:", waveContract.address);

// Initialize contractBalance
    let contractBalance = await hre.ethers.provider.getBalance(
        waveContract.address
    );

// Print Contract Balance
    console.log(
        "Contract Balance = ",
        hre.ethers.utils.formatEther(contractBalance)
    );

// Sending a test transaction
    let waveTxn = await waveContract.wave("Test message!");

// Waiting for the transaction to be mined    
    await waveTxn.wait();

    contractBalance = await hre.ethers.provider.getBalance(waveContract.address);
    console.log(
        "Contract Balance = ",
        hre.ethers.utils.formatEther(contractBalance)
    );

// Get output of AllWaves function (array of structs)
    let allWaves = await waveContract.getAllWaves();
    console.log(allWaves);
};

const runMain = async () => {
    try {
        await main();
        process.exit(0);
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
};

runMain();