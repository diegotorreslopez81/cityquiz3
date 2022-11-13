//SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/Base64.sol";
//import "hardhat/console.sol";

contract CityQuiz3 is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    constructor() ERC721("CityQuiz3", "CQ3") {}

    function mint(address player, string calldata _building, string calldata _quiz)
            public
        returns (uint256)
    {
        //console.log("This is mintCQ3 contract");

        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(player, newItemId);
        
        bytes memory svg = abi.encodePacked(
            '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400"><rect width="100%" height="100%" fill="black" />',
            '<text x="50%" y="15%" fill="white" dominant-baseline="middle" text-anchor="middle">&#127918; &#127961; CityQuiz3</text>'
            '<text x="50%" y="50%" fill="white" dominant-baseline="middle" text-anchor="middle" style="font-size:28px;">&#127941; Congratulations</text>'
            '<text x="50%" y="80%" fill="white" dominant-baseline="middle" text-anchor="middle">Building: ',
            _building,
            ', Quiz: ',
            _quiz,
            '</text>'
            '<text x="50%" y="90%" fill="white" dominant-baseline="middle" text-anchor="middle">User: 0x',
            Strings.toHexString(uint256(uint160(player)), 20),
            '</text>',
            '</svg>'
        );

        string memory imageStr = string(
            abi.encodePacked(
                "data:image/svg+xml;base64,",
                Base64.encode(svg)
            )    
        );
        //console.log("This is the SVG: %s", string(svg));
        delete svg;


        // Get all the JSON metadata in place and base64 encode it.
        string memory json = Base64.encode(
            bytes(
                string(
                    abi.encodePacked(
                        '{"name":"CityQuiz3 NFT", "image":"',
                        imageStr,
                        unicode'", "description": "This NFT marks the bound address as a member of the BuidlGuidl. The image is a fully-onchain dynamic SVG reflecting current balances of the bound wallet and builder work stream."}'
                    )
                )
            )
        );

        bytes memory image = abi.encodePacked(imageStr);
        delete imageStr;

        string memory tokenURI = string(
            abi.encodePacked(
                "data:application/json;base64,",
                json
            )    
        );
        delete image;
        
        //console.log("This is the tokenURI: %s", tokenURI);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }

}