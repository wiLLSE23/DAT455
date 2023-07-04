import numpy as np

#-----------Below is the encryption section------------
def textToBin(text):
    bin = []
    for c in text:
        bin.append(np.binary_repr(ord(c), width=8))
    return "".join(bin)

def binToInv(bin):
    code = []
    for b in bin:
        if(b == '1'):
            code.append('\t')
        else:
            code.append(' ')
    return "".join(code)

def encrypt(text):
    return binToInv(textToBin(text))

#-----------Below is the decryption section------------
def invToBin(inv):
    bin = []
    for bool in inv:
        if(bool == '\t'):
            bin.append('1')
        elif(bool == ' '):
            bin.append('0')
        else:
            pass
    return "".join(bin)

def binToText(bin):
    if(len(bin) % 8 != 0):
        print("error: binary cointains incomplete bytes")
    count = 0
    word = ""
    text = []
    for bit in bin:
        word += bit
        count+=1
        if(count==8):
            text.append(chr(binaryToDecimal(word)))
            word = ""
            count = 0
    return "".join(text)

def binToText2(bin):
    if(len(bin) % 8 != 0):
        print("error: binary cointains incomplete bytes")
    text = []
    while bin:
        print("word is ", bin[:8])
        text.append(chr(binaryToDecimal(bin[:8])))
        print(bin[8:])
        bin = bin[8:]
    return "".join(text)

def binaryToDecimal(d):
    decimal = 0
    len(d)
    for i in range(len(d)):
        if(abs(int(d[i])) > 1):
            return "error: input contains: " + d[i] + " which is invalid in binary"
        decimal += int(d[i]) * (2 ** (len(d) - i - 1))
    return decimal

def decrypt(inv):
    return binToText2(invToBin(inv))


print(decrypt(" \t  \t    \t\t  \t \t \t\t \t\t   \t\t \t\t   \t\t \t\t\t\t  \t    \t"))
print("Message is:[", encrypt("hello"), "]")
print(invToBin(" \t     \t"))