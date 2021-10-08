import secrets
import hashlib

count=0
while count<128:
#Boucle qui réessaye tant que la seed en binaire ne contient pas 128 bits
    count=0
    seed = secrets.randbits(128)
    print(seed)
    print(type(seed))




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

with open("wordList.txt", 'r') as list:
    wordList = [w.strip() for w in list.readlines()]

seed = []
for i in range(0,12,1):
    index = int(entropy[11*i:11*(i+1)],2)
    seed.append(wordList[index])
print(seed)