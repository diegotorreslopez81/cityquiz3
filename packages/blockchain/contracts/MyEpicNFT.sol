// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.1;

// We first import some OpenZeppelin Contracts.
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "hardhat/console.sol";

// We inherit the contract we imported. This means we'll have access
// to the inherited contract's methods.

contract MyEpicNFT is ERC721URIStorage {
    // Magic given to us by OpenZeppelin to help us keep track of tokenIds.
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    
    // This is our SVG code. All we need to change is the word that's displayed. Everything else stays the same.
    // So, we make a baseSvg variable here that all our NFTs can use.
    string baseSvg = "";

    // I create three arrays, each with their own theme of random words.
    // Pick some random funny words, names of anime characters, foods you like, whatever!
    string[] firstWords = ["YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD"];  
    string[] secondWords = ["YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD"];
    string[] thirdWords = ["YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD", "YOUR_WORD"];
    
    // We need to pass the name of our NFTs token and its symbol.
    constructor() ERC721 ("SquareNFT", "SQUARE") {
        console.log("This is my NFT contract. Woah!");
    }

    // I create a function to randomly pick a word from each array.
    function pickRandomFirstWord(uint256 tokenId) public view returns (string memory) {
        // I seed the random generator. More on this in the lesson.
        uint256 rand = random(string(abi.encodePacked("FIRST_WORD", Strings.toString(tokenId))));
        
        // Squash the # between 0 and the length of the array to avoid going out of bounds.
        rand = rand % firstWords.length;
        return firstWords[rand];
    }
    
    function pickRandomSecondWord(uint256 tokenId) public view returns (string memory) {
        uint256 rand = random(string(abi.encodePacked("SECOND_WORD", Strings.toString(tokenId))));
        rand = rand % secondWords.length;
        return secondWords[rand];
    }
    
    function pickRandomThirdWord(uint256 tokenId) public view returns (string memory) {
        uint256 rand = random(string(abi.encodePacked("THIRD_WORD", Strings.toString(tokenId))));
        rand = rand % thirdWords.length;
        return thirdWords[rand];
    }
    
    function random(string memory input) internal pure returns (uint256) {
        return uint256(keccak256(abi.encodePacked(input)));
    }
    
    function makeAnEpicNFT() public {
        uint256 newItemId = _tokenIds.current();
        // We go and randomly grab one word from each of the three arrays.
        string memory first = pickRandomFirstWord(newItemId);
        string memory second = pickRandomSecondWord(newItemId);
        string memory third = pickRandomThirdWord(newItemId);
        
        // I concatenate it all together, and then close the <text> and <svg> tags.
        string memory finalSvg = string(abi.encodePacked(baseSvg, first, second, third, "</text></svg>"));
        console.log("\n--------------------");
        console.log(finalSvg);console.log("--------------------\n");
        
        // Actually mint the NFT to the sender using msg.
        sender._safeMint(msg.sender, newItemId);
        
        // Set the NFTs data.
        _setTokenURI(newItemId, "data:application/json;base64,eyAgICAKIm5hbWUiOiAiRWdnIEhlYWQiLCAgICAgCiJkZXNjcmlwdGlvbiI6ICJBIG5ldyBORlQgY29sbGVjdGlvbiIsCiJpbWFnZSI6ICJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIzYVdSMGFEMGlNalF3SWlCb1pXbG5hSFE5SWpNeU1DSWdkbWxsZDBKdmVEMGlNQ0F3SURJME1DQXpNakFpSUdacGJHdzlJbTV2Ym1VaUlIaHRiRzV6UFNKb2RIUndPaTh2ZDNkM0xuY3pMbTl5Wnk4eU1EQXdMM04yWnlJK0NqeHdZWFJvSUdROUlrMHlNamdnTXpFNUxqVklNVEpETlM0Mk5EZzNNeUF6TVRrdU5TQXdMalVnTXpFMExqTTFNU0F3TGpVZ016QTRWakV5UXpBdU5TQTFMalkwT0RjeklEVXVOalE0TnpNZ01DNDFJREV5SURBdU5VZ3hOVGt1TVRjMVF6RTFPUzQxTnpFZ01DNDFJREUxT1M0NU5USWdNQzQyTlRZM05EZ2dNVFl3TGpJek15QXdMamt6TmpBeU1Vd3lNemt1TURVM0lEYzVMakkyT0RGRE1qTTVMak0wTVNBM09TNDFORGszSURJek9TNDFJRGM1TGprek1qWWdNak01TGpVZ09EQXVNek15TVZZek1EaERNak01TGpVZ016RTBMak0xTVNBeU16UXVNelV4SURNeE9TNDFJREl5T0NBek1Ua3VOVm9pSUdacGJHdzlJaU5HUmtZNVJqSWlJSE4wY205clpUMGlJMFpHUXpZNE1TSXZQZ284Y0dGMGFDQmtQU0pOTVRZd0xqVWdNUzR5TURjeE1Vd3lNemd1TnpreklEYzVMalZJTVRjeVF6RTJOUzQyTkRrZ056a3VOU0F4TmpBdU5TQTNOQzR6TlRFeklERTJNQzQxSURZNFZqRXVNakEzTVRGYUlpQm1hV3hzUFNJalJrWkdPVVl5SWlCemRISnZhMlU5SWlOR1JrTTJPREVpTHo0S1BIQmhkR2dnWkQwaVRUWTRMamcwTXpnZ01qUTBMakEzTWtNMk9TNHhOek00SURJMU1DNDJPVGtnTnpRdU56TTBOQ0F5TlRRdU9URTBJRGd6TGpFek9EY2dNalUwTGpreE5FTTVNaTR3TWpVMElESTFOQzQ1TVRRZ09UY3VOVE0xTWlBeU5UQXVORGsySURrM0xqVXpOVElnTWpRekxqTTROME01Tnk0MU16VXlJREl6Tnk0NE1qWWdPVFF1TkRFeU1TQXlNelF1TnpJNUlEZzJMamszTWpjZ01qTXpMakF5TjB3NE1pNDNOVGM0SURJek1pNHdOakpETnpndU1qRXlPU0F5TXpBdU9UazJJRGMyTGpNMU9UUWdNakk1TGpVME9TQTNOaTR6TlRrMElESXlOeTR3TXpWRE56WXVNelU1TkNBeU1qTXVPRFl4SURjNUxqRTFNak1nTWpJeExqYzNPU0E0TXk0ek5qY3lJREl5TVM0M056bERPRGN1TXpjNE9TQXlNakV1TnpjNUlEa3dMakl5TWpjZ01qSXpMamd6TmlBNU1DNDJOemszSURJeU55NHhNVEZJT1RZdU9UVXhNa001Tmk0Mk5EWTFJREl5TUM0NE5DQTVNUzR3T0RVNUlESXhOaTQwTkRjZ09ETXVNemt5TmlBeU1UWXVORFEzUXpjMUxqRTVNVFFnTWpFMkxqUTBOeUEyT1M0M05UYzRJREl5TUM0NE5qVWdOamt1TnpVM09DQXlNamN1TkRZM1F6WTVMamMxTnpnZ01qTXlMamtnTnpJdU9EZ3dPU0F5TXpZdU1UYzJJRGM1TGpVek16SWdNak0zTGpZNU9VdzROQzR5T0RFeUlESXpPQzQzT1RGRE9EZ3VPVGM0TlNBeU16a3VPRGd6SURrd0xqazRORFFnTWpReExqVXdPQ0E1TUM0NU9EUTBJREkwTkM0eE56UkRPVEF1T1RnME5DQXlORGN1TWprM0lEZzNMamcyTVRNZ01qUTVMalUxTnlBNE15NDFORFE1SURJME9TNDFOVGRETnpndU9EazROQ0F5TkRrdU5UVTNJRGMxTGpZME9EUWdNalEzTGpReU5DQTNOUzR5TkRJeUlESTBOQzR3TnpKSU5qZ3VPRFF6T0ZvaUlHWnBiR3c5SWlOR1JqaERNRElpTHo0S1BIQmhkR2dnWkQwaVRURXlNUzQxT1NBeU5UUk1NVE0wTGpJMklESXhOeTR6TmpGSU1USTNMakkzT0V3eE1UZ3VNVE0zSURJME5pNDFNVWd4TVRjdU56QTFUREV3T0M0ME9Ea2dNakUzTGpNMk1VZ3hNREV1TWpVeVRERXhOQzR3TkRrZ01qVTBTREV5TVM0MU9Wb2lJR1pwYkd3OUlpTkdSamhETURJaUx6NEtQSEJoZEdnZ1pEMGlUVEUzTUM0M016RWdNak01TGpNM05WWXlNelF1T0RBMVNERTFOUzQxTWpKV01qTTVMamd3TjBneE5qUXVNek16VERFMk5DNHpNRGNnTWpRd0xqVTJPRU14TmpRdU1qQTJJREkwTlM0M05EZ2dNVFl3TGpNNU55QXlORGt1TWpJM0lERTFOQzQ0TVRFZ01qUTVMakl5TjBNeE5EZ3VNamcySURJME9TNHlNamNnTVRRMExqRTVPQ0F5TkRRdU1EUTNJREUwTkM0eE9UZ2dNak0xTGpZeE4wTXhORFF1TVRrNElESXlOeTR6TVRRZ01UUTRMakl4SURJeU1pNHhNelVnTVRVMExqWXdPQ0F5TWpJdU1UTTFRekUxT1M0ek1EVWdNakl5TGpFek5TQXhOakl1TlRneElESXlOQzQwTnpFZ01UWXpMamt3TVNBeU1qZ3VOekV4U0RFM01DNDBNalpETVRZNUxqSTFPQ0F5TWpFdU1qUTJJREUyTXk0d05qTWdNakUyTGpRME55QXhOVFF1TmpBNElESXhOaTQwTkRkRE1UUTBMakUzTXlBeU1UWXVORFEzSURFek55NDBPVFVnTWpJekxqa3pPQ0F4TXpjdU5EazFJREl6TlM0Mk5qaERNVE0zTGpRNU5TQXlORGN1TlRJMUlERTBOQzR3T1RZZ01qVTBMamt4TkNBeE5UUXVOekVnTWpVMExqa3hORU14TmpRdU5EZzFJREkxTkM0NU1UUWdNVGN3TGpjek1TQXlORGd1T0RRMklERTNNQzQzTXpFZ01qTTVMak0zTlZvaUlHWnBiR3c5SWlOR1JqaERNRElpTHo0S1BIQmhkR2dnWm1sc2JDMXlkV3hsUFNKbGRtVnViMlJrSWlCamJHbHdMWEoxYkdVOUltVjJaVzV2WkdRaUlHUTlJazA1T1NBeE1UZERPVFl1Tnprd09TQXhNVGNnT1RVZ01URTRMamM1TVNBNU5TQXhNakZXTVRRNExqa3pPVU01TkM0ek16ZzJJREUwT0M0NU56a2dPVE11TmpjeE55QXhORGtnT1RNZ01UUTVRemMxTGpNeU5qa2dNVFE1SURZeElERXpOQzQyTnpNZ05qRWdNVEUzUXpZeElEazVMak15TmprZ056VXVNekkyT1NBNE5TQTVNeUE0TlVNeE1UQXVOamN6SURnMUlERXlOU0E1T1M0ek1qWTVJREV5TlNBeE1UZElPVGxhVFRFeU5TQXhNVGRJTVRVMVF6RTFOeTR5TURrZ01URTNJREUxT1NBeE1UZ3VOemt4SURFMU9TQXhNakZXTVRjM1F6RTFPU0F4TnprdU1qQTVJREUxTnk0eU1Ea2dNVGd4SURFMU5TQXhPREZJT1RsRE9UWXVOemt3T1NBeE9ERWdPVFVnTVRjNUxqSXdPU0E1TlNBeE56ZFdNVFE0TGprek9VTXhNVEV1TnpReElERTBOeTQ1TURZZ01USTFJREV6TkM0d01ERWdNVEkxSURFeE4xb2lJR1pwYkd3OUlpTkdSa00yT0RFaUx6NEtQQzl6ZG1jK0NnPT0iIAp9");

        console.log("An NFT w/ ID %s has been minted to %s", newItemId, msg.sender);
        // Increment the counter for when the next NFT is minted.
        _tokenIds.increment();
    }
}