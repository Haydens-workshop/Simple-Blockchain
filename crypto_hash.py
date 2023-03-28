import hashlib
import json
import os

def crypto_hash(*args):
    # Generate a random salt
    salt = os.urandom(16)

    # Serialize the arguments and add the salt
    serialized_args = json.dumps(args, sort_keys=True).encode('utf-8') + salt

    # Generate a HMAC using SHA-256 and the salt as the key
    hmac = hashlib.sha256(salt).digest()

    # Hash the serialized arguments using SHA-256
    hashed_data = hashlib.sha256(serialized_args).digest()

    # Concatenate the HMAC and the hashed data
    result = hmac + hashed_data

    # Encode the result as a hexadecimal string
    return result.hex()

def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash('2', 'one', [3]): {crypto_hash('2', 'one', [3])}")

if __name__ == '__main__':
    main()
