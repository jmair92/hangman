import random
words = ["python", "java", "kotlin", "javascript"]
random.seed()
choice = random.choice(words)
turns = 8
guessed_letters = []
word_so_far = list("-" * len(choice))
word_as_string = ''.join(word_so_far)
print('H A N G M A N')
play = input('Type "play" to play the game, "exit" to quit:')
while play == "play":
    print("")
    print(word_as_string)
    letter = input("Input a letter:")
    while turns > 0:
        if len(letter) == 1:
            if letter.isalpha() and letter.islower():
                if letter in guessed_letters:
                    print("You've already guessed this letter")
                elif letter in choice:
                    for i in range(0, len(choice)):
                        if letter == choice[i]:
                            word_so_far[i] = letter
                            word_as_string = ''.join(word_so_far)
                    guessed_letters.append(letter)
                else:
                    print("That letter doesn't appear in the word")
                    turns = turns - 1
                    guessed_letters.append(letter)
            else:
                print("Please enter a lowercase English letter")
        else:
            print("You should input a single letter")
        if turns == 0:
            print("You lost!")
            break
        else:
            print("")
            print(word_as_string)
        if word_as_string.isalpha():
            print("You guessed the word!")
            print("You survived!")
            break
        else:
            letter = input("Input a letter:")
    play = input('Type "play" to play the game, "exit" to quit:')
