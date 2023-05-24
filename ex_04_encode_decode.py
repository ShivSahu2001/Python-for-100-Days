import string
import random

def encodeStr():

    strData = input("Enter a string to encode: ")

    if(len(strData) < 3):
        print(strData[::-1])
    else:
        fChar = strData[0:1]
        nChar = strData[1:]
        newStr = "".join((nChar,fChar))
        # print(newStr)
        randomStart = "".join(random.choices(string.ascii_lowercase,k=3))
        randomEnd =  "".join(random.choices(string.ascii_lowercase,k=3))

        bigStrEncode = "".join((randomStart, newStr, randomEnd))
        print(bigStrEncode)


def decodeStr():
    strData = input("Enter a string to decode: ")

    if(len(strData) < 3):
        print(strData[::-1])
    else:
        # fChar = strData[-1]
        # nChar = strData[0:len(strData)-1]
        # print(fChar)
        # print(nChar)
        # newStr = "".join((fChar,nChar))
        # newStr = fChar+nChar
        # print(newStr)
        # rmFirstThreeChar = strData[0:3]
        # rmLastThreeChar = strData[:-3]
        fChar = strData[3:-4]
        fChars = str(fChar)
        nChar = strData[-4]
        nChars = str(nChar)
        joinStr = "".join([nChars,fChars])
        print(joinStr)

# btjhivsiuk
# ajr

encodeStr()
decodeStr()