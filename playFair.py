import numpy as np 
import string
from collections import OrderedDict

# Getting Input key word

keyText = (input("Enter the key text:-")).upper()
keyArray = np.array([])
keyText = "".join([char for char in OrderedDict.fromkeys(keyText.replace("J", "I"))])
alphabetString = (string.ascii_uppercase).replace("J", "")

for x in alphabetString:
    if x not in keyText:
        keyText = keyText + x

keyArray = (np.append(keyArray, [char for char in keyText])).reshape(5, 5)

# Getting Input plain text

plainText = ""
rawPlainText = input("Enter the plain text:-")
rawPlainText.replace("J", "I")
for x in rawPlainText:
    if len(plainText) != 0 and x == plainText[len(plainText) - 1]:
        plainText = plainText + 'x' + x
    else:
        plainText = plainText + x
if len(plainText) % 2 != 0:
    plainText = plainText + 'z'

plainText = (np.array([char.upper() for char in plainText])).reshape(int(len(plainText)/2), 2)

def enDecode(codeText, cmpLength, maxLength, typeCode):
    result = ""
    for x in codeText:
        i, j = np.where(keyArray == x[0])
        k, l = np.where(keyArray == x[1])
        if j == l:
            if i == (cmpLength):
                result = result + (keyArray[(maxLength), j])[0] + (keyArray[abs((-k)+typeCode), l])[0]
            elif k == (cmpLength):
                result = result + (keyArray[abs((-i)+typeCode), j])[0] + (keyArray[(maxLength), l])[0]
            else:
                result = result + (keyArray[abs((-i)+typeCode), j])[0] + (keyArray[abs((-k)+typeCode), l])[0]
        elif i == k:
            if j == (cmpLength):
                result = result + (keyArray[i, (maxLength)])[0] + (keyArray[k, abs((-l)+typeCode)])[0]
            elif l == (cmpLength):
                result = result + (keyArray[i, abs((-j)+typeCode)])[0] + (keyArray[k, (maxLength)])[0]
            else:
                result = result + (keyArray[i, abs((-j)+typeCode)])[0] + (keyArray[k, abs((-l)+typeCode)])[0]
        else:
            result = result + (keyArray[i, l])[0] + (keyArray[k, j])[0]
    if typeCode == 1:
        if 'X' in result:
            result = result.replace("X", "")
        if 'Z' in result:
            result = result.replace("Z" , "")
    return result

print("Encoded Text is:-", (enDecode(plainText, (len(keyArray) - 1), 0, -1)).lower())

encodedText = input("Enter encoded Text:-")

encodedText = (np.array([char.upper() for char in encodedText])).reshape(int(len(encodedText)/2), 2)

print("Decoded Text is:-", (enDecode(encodedText, 0, (len(keyArray) - 1), 1)).lower())