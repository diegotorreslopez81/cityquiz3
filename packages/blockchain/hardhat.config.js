require("@nomicfoundation/hardhat-toolbox");

//
// Select the network you want to deploy to here:
//
const defaultNetwork = "localhost";


/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.17",
  defaultNetwork,
  allowUnlimitedContractSize: true,
  // don't forget to set your provider like:
  // REACT_APP_PROVIDER=https://dai.poa.network in packages/react-app/.env
  // (then your frontend will talk to your contracts on the live network!)
  // (you will need to restart the `yarn run start` dev server after editing the .env)

  networks: {
    hardhat:{},
    localhost: {
      url: "http://localhost:8545",
      allowUnlimitedContractSize: true,
      gasPrice: 1500000000,
      gas: 6000000,
      /*
        notice no mnemonic here? it will just use account 0 of the hardhat node to deploy
        (you can put in a mnemonic here to set the deployer locally)
      */
    },
    goerli: {
      url: "https://goerli.infura.io/v3/bb5ae532dc9441c7bc43ab328d4ff895", //<---- YOUR INFURA ID! (or it won't work)
      accounts: ["e32bc5b6f539fac9d887c1ba054792afcd0d81315ba63676bfbb2aeab9ce9e14"],
    },

    // mainnet: {
    //   url: "https://mainnet.infura.io/v3/bb5ae532dc9441c7bc43ab328d4ff895", //<---- YOUR INFURA ID! (or it won't work)
    //   accounts: {
    //     mnemonic: mnemonic(),
    //   },
    // },

    // xdai: {
    //   url: 'https://rpc.xdaichain.com/',
    //   gasPrice: 1000000000,
    //   accounts: {
    //     mnemonic: mnemonic(),
    //   },
    // },
    // matic: {
    //   url: 'https://rpc-mainnet.maticvigil.com/',
    //   gasPrice: 1000000000,
    //   accounts: {
    //     mnemonic: mnemonic(),
    //   },
    // },
  },
  etherscan: {
    // Your API key for Etherscan
    // Obtain one at https://etherscan.io/
    apiKey: "ZK56QMKEAPIFZ6RPDB8SNKQQRVMZU1EKT5"
  }
};