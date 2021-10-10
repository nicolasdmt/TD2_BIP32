import secrets
import hashlib

def enterMnemonic ():
    mnemonic = []
    for i in range(0,12):
        mnemonic.append(input())
    return mnemonic

def creationEntropy (mnemonic):
    with open("wordList2.txt", 'r') as list:
        wordList = [w.strip() for w in list.readlines()]

    entropy = ""
    for i in range(0, 12, 1):
        for j in range(0,2048):
            if j<10:
                if mnemonic[i]==wordList[j][12:]:
                    entropy += wordList[j][1:13]
            elif j<100:
                if mnemonic[i]==wordList[j][13:]:
                    entropy += wordList[j][2:14]
            elif j<1000:
                if mnemonic[i]==wordList[j][14:]:
                    entropy += wordList[j][3:15]
            else:
                if mnemonic[i]==wordList[j][15:]:
                    entropy += wordList[j][4:16]
    return entropy

if __name__ == '__main__':
    mnemonic = enterMnemonic()
    entropy = creationEntropy(mnemonic)
    print(entropy)
