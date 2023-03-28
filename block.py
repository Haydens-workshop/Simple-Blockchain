from datetime import datetime
from crypto_hash import crypto_hash

DIFFICULTY = 4
NONCE_RANGE = range(100000)

class Block:
    def __init__(self, timestamp, last_hash, hash, transactions, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.transactions = transactions
        self.nonce = nonce

    def __repr__(self):
        return (
            f'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'transactions: {self.transactions}, '
            f'nonce: {self.nonce})'
        )

    @staticmethod
    def mine_block(last_block, transactions):
        timestamp = datetime.now()
        last_hash = last_block.hash
        nonce = Block.find_nonce(last_hash, transactions)
        hash = crypto_hash(timestamp, last_hash, transactions, nonce)
        return Block(timestamp, last_hash, hash, transactions, nonce)

    @staticmethod
    def find_nonce(last_hash, transactions):
        for nonce in NONCE_RANGE:
            hash = crypto_hash(last_hash, transactions, nonce)
            if hash.startswith('0' * DIFFICULTY):
                return nonce
        raise ValueError("No valid nonce found")

    @staticmethod
    def genesis():
        return Block(
            timestamp=datetime.now(),
            last_hash='genesis_last_hash',
            hash='genesis_hash',
            transactions=[],
            nonce=0
        )

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

