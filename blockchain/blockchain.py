from block import Block
from crypto_hash import crypto_hash

class Blockchain:

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')

from datetime import datetime
from crypto_hash import crypto_hash

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.timestamp = datetime.now()
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {
            'timestamp': self.timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }

class Block:
    def __init__(self, timestamp, last_hash, hash, transactions):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.transactions = transactions

    def __repr__(self):
        return (
            f'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'transactions: {self.transactions})'
        )

    @staticmethod
    def mine_block(last_block, transactions):
        timestamp = datetime.now()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, transactions)
        return Block(timestamp, last_hash, hash, transactions)

    @staticmethod
    def genesis():
        return Block(
            timestamp=datetime.now(),
            last_hash='genesis_last_hash',
            hash='genesis_hash',
            transactions=[]
        )

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, [Transaction('sender1', 'recipient1', 10), Transaction('sender2', 'recipient2', 20)])
    print(block)

if __name__ == '__main__':
    main()
