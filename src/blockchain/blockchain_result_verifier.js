const ethers = require('ethers');

class BlockchainResultVerifier {
    constructor(contractAddress, contractABI, providerUrl) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.contract = new ethers.Contract(contractAddress, contractABI, this.provider);
    }

    async verifyResult(resultHash, timestamp) {
        try {
            const verificationResult = await this.contract.verifyResult(resultHash, timestamp);
            return verificationResult;
        } catch (error) {
            console.error("Verification failed:", error);
            return false;
        }
    }

    async recordResult(resultHash) {
        try {
            const signer = this.provider.getSigner();
            const tx = await this.contract.connect(signer).recordResult(resultHash);
            await tx.wait();
            console.log("Result recorded on blockchain");
            return true;
        } catch (error) {
            console.error("Recording failed:", error);
            return false;
        }
    }
}

module.exports = BlockchainResultVerifier;