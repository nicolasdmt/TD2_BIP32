import secrets
import hashlib

bits = secrets.randbits(128)
print(bits)
bits_hex = hex(bits)[2:]
print(bits_hex)
bits_enc = bits_hex.encode()
print(bits_enc)
bits_hash = hashlib.sha256(bits_enc)
print(bits_hash.hexdigest())
