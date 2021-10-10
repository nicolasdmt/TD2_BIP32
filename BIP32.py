from mnemonic import Mnemonic
import bip32utils
mnemon = Mnemonic('english')
words = mnemon.generate(256)
print(words)
mnemon.check(words)
seed = mnemon.to_seed(words)
print(f'BIP39 Seed: {seed.hex()}\n')
root_key = bip32utils.BIP32Key.fromEntropy(seed)
chain_code = root_key.ChainCode().hex()
root_public_hex = root_key.PublicKey().hex()
root_private_hex = root_key.PrivateKey().hex()

print('Root key:')
print(f'\tChain code: {chain_code}')
print(f'\tPublic : {root_public_hex}')
print(f'\tPrivate : {root_private_hex}')

child_key = root_key.ChildKey(0)
child_public_hex = child_key.PublicKey().hex()
child_private_hex = child_key.PrivateKey().hex()

print('Child key m/0/0:')
print(f'\tPublic : {child_public_hex}')
print(f'\tPrivate: {child_private_hex}\n')