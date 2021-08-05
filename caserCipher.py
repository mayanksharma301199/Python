import string

caserKey = int(input("Enter the caser key:-"))
alphabetString = string.ascii_uppercase

def enDecode(codeText, expression, limit):
    text = ""
    for char in codeText:
        charPosition = alphabetString.find(char)
        if eval(expression) > limit:
            text += alphabetString[abs(eval(expression) - 26)]
        else:
            text += alphabetString[abs(eval(expression))]
    return text

caserText = (input("Enter the text to encode:-")).upper()
print("Encoded text is:-", enDecode(caserText, "caserKey + charPosition", 25))

decodeText = (input("Enter the text to decode:-")).upper()
print("Decoded text is:-", enDecode(decodeText, "caserKey - charPosition", 0))