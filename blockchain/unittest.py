import unittest
from datetime import datetime
from crypto_hash import crypto_hash
from block import Block, Transaction

class TestBlock(unittest.TestCase):

    def test_mine_block(self):
        genesis_block = Block.genesis()
        block = Block.mine_block(genesis_block, [Transaction('sender1', 'recipient1', 10), Transaction('sender2', 'recipient2', 20)])

        self.assertIsInstance(block, Block)
        self.assertEqual(block.last_hash, genesis_block.hash)
        self.assertIsInstance(block.timestamp, datetime)
        self.assertIsInstance(block.hash, str)
        self.assertEqual(len(block.transactions), 2)

    def test_genesis(self):
        genesis_block = Block.genesis()

        self.assertIsInstance(genesis_block, Block)
        self.assertEqual(genesis_block.last_hash, 'genesis_last_hash')
        self.assertIsInstance(genesis_block.timestamp, datetime)
        self.assertEqual(genesis_block.hash, 'genesis_hash')
        self.assertEqual(len(genesis_block.transactions), 0)

class TestTransaction(unittest.TestCase):

    def test_to_dict(self):
        transaction = Transaction('sender', 'recipient', 100)

        self.assertIsInstance(transaction.to_dict(), dict)
        self.assertEqual(transaction.to_dict()['sender'], 'sender')
        self.assertEqual(transaction.to_dict()['recipient'], 'recipient')
        self.assertEqual(transaction.to_dict()['amount'], 100)

if __name__ == '__main__':
    unittest.main()
