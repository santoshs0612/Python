# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random

def encodeLogic(w):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    front = ''.join(random.choice(chars) for _ in range(3))
    back = ''.join(random.choice(chars) for _ in range(3))
    newWord = front+w[1:]+w[0]+back
    return newWord
def decodeLogic(w):
    word = w[3:-3]
    word= word[-1]+word[:-1]
    return word
def encoder(inputString):
    words = inputString.split(" ")
    codeword =[]
    for w in words:
        if len(w)<3:
            codeword.append(w[::-1])
        else:
            codeword.append(encodeLogic(w))

    encodedString=""
    for w in codeword:
        encodedString= encodedString+w+" "
    # print(encodedString)
    return encodedString
def decoder(decodeString):
    words = decodeString.strip().split(" ")
    # print(words)
    codeword =[]
    for w in words:
        if len(w)<3:
            codeword.append(w[::-1])
        else:
            codeword.append(decodeLogic(w))
    newdecodeString=""
    for w in codeword:
        newdecodeString= newdecodeString+w+" "
    
    # print(newdecodeString)
    return newdecodeString


print("Welcome to the Secret language systems:")

print("         Enter your string you want to encode")

# inputString = "Hi Santosh are you looking for me"
inputString = input()

encodededString = encoder(inputString)
print("Your Encoded string is: ",encodededString)

decodedString = decoder(encodededString)
print(decodedString)


