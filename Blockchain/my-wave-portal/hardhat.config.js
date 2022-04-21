require("@nomiclabs/hardhat-waffle");

module.exports = {
  solidity: "0.8.4",
  networks: {
    rinkeby: {
      url: "https://eth-rinkeby.alchemyapi.io/v2/vo2N2ne5nmkQxdyJufTbl3gqeKZ5V6W8",
      accounts: ["2f985a18f074432ed09a2aecd355af8ba2eacc994a180a60dcd925e73cafec41"]
    },
  },
};
