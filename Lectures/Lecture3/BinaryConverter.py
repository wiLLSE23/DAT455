import math

def binaryToDecimal(d):
    decimal = 0
    len(d)
    for i in range(len(d)):
        if(abs(int(d[i])) > 1):
            return "error: input contains: " + d[i] + " which is invalid in binary"
        decimal += int(d[i]) * (2 ** (len(d) - i - 1))
    return decimal

#Testing below
def main():
    print("running function")
    print(binaryToDecimal('0'))
    print(binaryToDecimal('10000111'))
    print(binaryToDecimal('102'))

main()
