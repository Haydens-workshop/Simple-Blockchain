import json
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256



# signs a transaction using the private key of the sender.
# transaction object and the private key as inputs&returns signature as hex string.
def sign_transaction(transaction, private_key):
    # Convert transaction object to dictionary and serialize as a JSON string.
    transaction_dict = transaction.to_dict()
    transaction_json = json.dumps(transaction_dict, sort_keys=True).encode()

    
    #Hash the serialized transaction using the SHA-256 hash algorithm.
def sign_transaction(transaction, private_key):
    transaction_dict = transaction.to_dict()
    transaction_json = json.dumps(transaction_dict, sort_keys=True).encode()
    hashed_transaction = SHA256.new(transaction_json)
    signature = pkcs1_15.new(private_key).sign(hashed_transaction)
    return signature.hex()

def verify_signature(public_key, signature, transaction_dict):
    transaction_json = json.dumps(transaction_dict, sort_keys=True).encode()
    hashed_transaction = SHA256.new(transaction_json)
    try:
        signature_bytes = bytes.fromhex(signature)
        pkcs1_15.new(public_key).verify(hashed_transaction, signature_bytes)
        return True
    except (ValueError, TypeError):
      #If signature invalid--the function will raise a ValueError or TypeError, and the function should return as false.
        return False
