// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts@4.8.2/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts@4.8.2/access/Ownable.sol";
import "@openzeppelin/contracts@4.8.2/utils/Counters.sol";

contract Zksync2023 is ERC721, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    uint256 MAX_SUPPLY = 100;
    // uint256 MAX_PER_WALLET = 1;
    // string baseURI = "ipfs://QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/"; 猴子不用+baseExtension
    string baseURI = "ipfs://QmWdEMPmo8d5rcXVrLkcT895rqFt6k6tJcL5DGqW5ASffv/";
    string baseExtension = ".json";
    // uint256 public mint_price = 0.0001 ether;
    
    mapping (address => bool) public mintedWallets;

    constructor() ERC721("zksync2023", "zk2023") {}


    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(
            _exists(tokenId),
            "ERC721Metadata: URI query for nonexistent token"
        );
        // return string(abi.encodePacked(baseURI, Strings.toString(tokenId)));
        return string(abi.encodePacked(baseURI, Strings.toString(tokenId), baseExtension));
    }

    function safeMint() payable public {
        uint256 tokenId = _tokenIdCounter.current();
        require (tokenId < MAX_SUPPLY,"sorry, sold out.");
        require (mintedWallets[msg.sender] == false,"sorry, you only can mint once.");
        // require (msg.value >= mint_price,"you do not have enough eth." );
        _tokenIdCounter.increment();
        mintedWallets[msg.sender] = true;
        _safeMint(msg.sender, tokenId);
    }
}