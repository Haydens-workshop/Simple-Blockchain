import hashlib
import hmac
import json
import os

def crypto_hash(*args, key=None):
    """
    Return a SHA-256 hash of given arguments using HMAC-SHA256.
    """
    if key is None:
        key = os.environ.get('HMAC_SECRET_KEY')
        if key is None:
            raise ValueError("HMAC secret key not found.")
    key = key.encode('utf-8')

    message = json.dumps(args, sort_keys=True).encode('utf-8')
    hmac_hash = hmac.new(key, message, hashlib.sha256).digest()
    return hmac_hash.hex()

def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash('2', 'one', [3]): {crypto_hash('2', 'one', [3])}")

if __name__ == '__main__':
    main()
