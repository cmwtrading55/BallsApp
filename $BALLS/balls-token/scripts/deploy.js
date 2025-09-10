const hre = require("hardhat");

async function main() {
  console.log("Deploying $BALLS token...");

  const BallsToken = await hre.ethers.getContractFactory("BallsToken");
  const ballsToken = await BallsToken.deploy();

  await ballsToken.waitForDeployment();

  const address = await ballsToken.getAddress();
  console.log("$BALLS token deployed to:", address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  }); 