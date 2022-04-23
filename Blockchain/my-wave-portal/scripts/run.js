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

    const waveTxn = await waveContract.wave("This is 1");
    await waveTxn.wait();

    const waveTxn2 = await waveContract.wave("This is 2");
    await waveTxn2.wait();

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