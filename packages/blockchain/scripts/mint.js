require("@nomiclabs/hardhat-ethers");
const contract = require("../artifacts/contracts/MyEpicNFT.sol/MyEpicNFT.json");
const contractInterface = contract.abi;
const contractAddress = "0x78a9c881339b69463bfF11b4817Ff6EF44b2782B";

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
    .makeAnEpicNFT()
    .then((tx) => tx.wait(5))
    .then((receipt) => console.log(`Confirmed! Your transaction receipt is: ${receipt.transactionHash}`))
    .catch((e) => console.log("Something went wrong", e));
};

main();