import string 

alphabeticString = string.ascii_uppercase

def enDecode(codeText, expression, limit):
    text = ""
    for index in range(len(codeText)):
        charPosition = alphabeticString.find(codeText[index])
        keyPosition = alphabeticString.find(keyWord[index])
        if eval(expression) > limit:
            text += alphabeticString[abs(eval(expression) - 26)]
        else:
            text += alphabeticString[abs(eval(expression))]
    return text

keyWord = input("Enter the keyWord:-").upper()
text = input("Entet the text to encode:-").upper()

if len(keyWord) < len(text):
    for i in range(len(text) - len(keyWord)):
        keyWord += keyWord[i]
else:
    keyWord = keyWord[len(text)]

print("Encoded text is:-", enDecode(text, "keyPosition + charPosition", 25))
text = input("Entet the text to decode:-").upper()
print("Decoded text is:-", enDecode(text, "keyPosition - charPosition", 0))