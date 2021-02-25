string = input()
for mark in [".", ",", "!", "?"]:
    string = string.replace(mark, "")
string = string.lower()
print(string)
