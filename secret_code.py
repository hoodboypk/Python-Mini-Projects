# Coding

str = input("Enter the message: ")
words = str.split(" ")
coding = input("Enter 1 for coding, 0 for decoding: ")
coding = True if coding == "1" else False    
if(coding):
    nword = []
    r1 = input("Enter random 3 letter word: ")
    r2 = input("Enter random 3 letter word: ")
    for word in words:
        if(len(word)>=3):
            strnew = r1 + word[1:] + word[0] + r2
            nword.append(strnew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))

# decoding
else:
    nword = []
    for word in words:
        if(len(word)>=3):
            strnew = word[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            nword.append(strnew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))