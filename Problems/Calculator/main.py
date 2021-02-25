first = float(input())
second = float(input())
operator = input()

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    print(first / second if second != 0 else "Division by 0!")
elif operator == "*":
    print(first * second)
elif operator == "mod":
    print(first % second if second != 0 else "Division by 0!")
elif operator == "pow":
    print(first ** second)
elif operator == "div":
    print(first // second if second != 0 else "Division by 0!")
