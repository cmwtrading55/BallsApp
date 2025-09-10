const { ethers } = require('ethers');

const urls = [
  'https://polygon-rpc.com',
  'https://polygon.llamarpc.com',
  'https://rpc.ankr.com/polygon',
];

function makeProvider(retries = 1) {
  let index = 0;
  async function getProvider() {
    for (let i = 0; i <= retries; i++) {
      try {
        const p = new ethers.providers.JsonRpcProvider(urls[index % urls.length], 137);
        await p.getBlockNumber();                  // quick health check
        return p;
      } catch {
        index++;                                   // rotate and retry
      }
    }
    throw new Error('All Polygon public RPCs failed');
  }
  return getProvider();
}

module.exports = { makeProvider }; 