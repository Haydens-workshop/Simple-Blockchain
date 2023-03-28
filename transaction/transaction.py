from datetime import datetime
from signature import verify_signature

class Transaction:
    def __init__(self, sender, recipient, amount, signature=None):
        self.timestamp = datetime.now()
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_dict(self):
        return {
            'timestamp': self.timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }

    def sign(self, private_key):
        self.signature = sign_transaction(self, private_key)

    def __repr__(self):
        return (
            f'Transaction('
            f'timestamp: {self.timestamp}, '
            f'sender: {self.sender}, '
            f'recipient: {self.recipient}, '
            f'amount: {self.amount}, '
            f'signature: {self.signature})'
        )
