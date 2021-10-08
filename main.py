import secrets
import hashlib

count=0
while count<128:
#Boucle qui réessaye tant que la seed en binaire ne contient pas 128 bits
    count=0
    seed = secrets.randbits(128)
    print(seed)

    genEntropy = bin(seed)[2:]
    print(genEntropy)

    for i in genEntropy:
        count += 1

print(count)

seedEnc = genEntropy.encode()
seedHash = hashlib.sha256(seedEnc)
print(seedHash.hexdigest())

int_seedHash = int(seedHash.hexdigest(), base=16)

seedHash2 = bin(int_seedHash)[2:]
print(seedHash2)

checkSum = ""
for i in range(0,4) :
    checkSum += seedHash2[i]
print(checkSum)

entropy = genEntropy + checkSum
print(entropy)
print(len(entropy))

