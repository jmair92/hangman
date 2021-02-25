n = input()
for i in n:
    if i.isalpha():
        if i in "a, e, i, o, u":
            print("vowel")
        else:
            print("consonant")
    else:
        break
