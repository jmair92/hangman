word = input()
final_string = word[0].lower()

for i in word[1:]:
    if i.isupper():
        final_string += "_"
    final_string += i.lower()

print(final_string)
