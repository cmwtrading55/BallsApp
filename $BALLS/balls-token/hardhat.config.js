require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

module.exports = {
  solidity: "0.8.20",
  defaultNetwork: "polygon",
  networks: {
    polygon: {
      url: process.env.RPC_URL || "https://polygon-rpc.com",
      chainId: 137,
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    },
  },
  etherscan: {
    apiKey: "KCD4R3MSY7TJDDJYTSSM6WE8JBWK7GRPJA",
  },
}; 