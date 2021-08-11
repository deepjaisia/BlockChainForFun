import  hashlib

class BlockChain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        gensisBlock = Block(0, "2021-08-10T06:16:51Z", TransactionData("Zenyatta", "Genji", 0), "FirstHash")
        return gensisBlock

    def getLatestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calcHash()
        self.chain.append(newBlock)
    
    def checkChainValidity(self):
        # TO DO

class Block:
    def __init__(self, index, timestamp, data, previousHash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calcHash()

    def calcHash(self):
        return(hashlib.sha256(str(str(self.index) + str(self.timestamp) + str(self.previousHash) + str(self.data)).encode('utf-8')))

class TransactionData:
    def __init__(self, sender, receiver, amount: int):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

# Manual Testing of BlockChain
djCoin = BlockChain()
firstPaymentBlock = djCoin.addBlock(Block(1, '2021-08-11T06:16:51Z', TransactionData("Genji", "McCree", 1)))
secondPaymentBlock = djCoin.addBlock(Block(2, '2021-08-12T06:16:51Z', TransactionData("McCree", "Tracer", 2)))
latestBlock = djCoin.getLatestBlock()
# print(latestBlock.hash.hexdigest())
# print(latestBlock.previousHash.hexdigest())
print(djCoin.chain)