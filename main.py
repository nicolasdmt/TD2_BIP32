import secrets
import hashlib
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

def creationGenEntropy ():
    count = 0
    while count < 128:
        # Boucle qui réessaye tant que la seed en binaire ne contient pas 128 bits
        count = 0
        seed = secrets.randbits(128)

        genEntropy = bin(seed)[2:]

        for i in genEntropy:
            count += 1
    return genEntropy

def sha256 (genEntropy):
    seedEnc = genEntropy.encode()
    seedHash = hashlib.sha256(seedEnc)

    int_seedHash = int(seedHash.hexdigest(), base=16)

    hash = bin(int_seedHash)[2:]
    return hash

def creationEntropy (genEntropy, hash):
    checkSum = ""
    for i in range(0, 4):
        checkSum += hash[i]

    entropy = genEntropy + checkSum
    return entropy

def creationMnemonic (entropy):
    with open("wordList.txt", 'r') as list:
        wordList = [w.strip() for w in list.readlines()]

    mnemonic = ""
    for i in range(0, 12, 1):
        index = int(entropy[11 * i:11 * (i + 1)], 2)
        mnemonic = mnemonic + wordList[index] + " "
    return mnemonic

if __name__ == '__main__':
    genEntropy = creationGenEntropy()
    hash = sha256(genEntropy)
    entropy = creationEntropy(genEntropy, hash)
    mnemonic = creationMnemonic(entropy)
    print("The twelve word mnemonic code created is : \n" + mnemonic)