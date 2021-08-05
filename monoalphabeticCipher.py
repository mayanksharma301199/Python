import string

alphabeticString = string.ascii_uppercase
cipherText = "QWERTYUIOPASDFGHJKLZXCVBNM"

def enDecode(text, findString, getString):
    result = ""
    for char in text:
         result += " " if char == " " else eval(getString)[eval(findString).find(char)]
    return result

text = input("Enter to encode the text:-").upper()
print("Encoded text is:-", enDecode(text, "alphabeticString", "cipherText"))

text = input("Enter to decode the text:-").upper()
print("Decoded text is:-", enDecode(text, "cipherText", "alphabeticString"))