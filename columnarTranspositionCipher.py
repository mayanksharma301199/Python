import numpy as np
import math

keyWord = input("Enter the keyWord:-").upper()
plainText = input("Enter the text for encryption:-").upper()
rngValue = "math.ceil((({text})/(len(keyWord))))"
textArr = np.array([])

def makeArr(rngValue, text, arr):
    for index in range(eval(rngValue) * len(keyWord)):
        if index >= len(eval(text)):
            arr = np.append(arr, "_")
        else:
            arr = np.append(arr, eval(text)[index])
    return arr.reshape(eval(rngValue), len(keyWord))

def enDecode(textArr, column, row):
    text = ""
    for currentColumn in column:
        for currentRow in row:
            text += textArr[currentRow, currentColumn]
    return text
textArr = makeArr(rngValue.format(text = len(plainText)), "plainText", textArr)
print("Encoded text is:-", enDecode(textArr, np.argsort(np.array([char for char in keyWord])), range(eval(rngValue.format(text = len(plainText))))))

decodeText = (input("Enter text for decodeing:-")).upper()
textArr = np.array([])

textArr = makeArr(rngValue.format(text = len(decodeText)), "decodeText", textArr)
print("Decoded text is:-", (enDecode(textArr, range(len(keyWord)), [(str(''.join(sorted(keyWord)))).find(char) for char in keyWord])).replace("_", ""))