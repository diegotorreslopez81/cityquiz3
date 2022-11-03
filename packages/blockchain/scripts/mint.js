require("@nomiclabs/hardhat-ethers");
const contract = require("../artifacts/contracts/CityQuiz3NFT.sol/CityQuiz3.json");
const contractInterface = contract.abi;
const contractAddress = "0x5FbDB2315678afecb367f032d93F642f64180aa3";

let provider = ethers.provider;

// const tokenCID = "https://bafkreifvtwuiypleu4vv7edh4zclmymp5ixh44xxmd3hb2imiqa7mp2c3a.ipfs.dweb.link/";
const privateKey = `0xe32bc5b6f539fac9d887c1ba054792afcd0d81315ba63676bfbb2aeab9ce9e14`;
const wallet = new ethers.Wallet(privateKey);

wallet.provider = provider;
const signer = wallet.connect(provider);

const nft = new ethers.Contract(
    contractAddress,
    contractInterface,
    signer
);

const main = () => {
  console.log("Waiting for 5 blocks to confirm...");
  nft
    .mint("0x1CBd3b2770909D4e10f157cABC84C7264073C9Ec")
    .then((tx) => tx.wait(5))
    .then((receipt) => console.log(`Confirmed! Your transaction receipt is: ${receipt.transactionHash}`))
    .catch((e) => console.log("Something went wrong", e));
};

main();