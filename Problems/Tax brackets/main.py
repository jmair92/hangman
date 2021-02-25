income = int(input())
if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25
else:
    percent = 28
if percent != 0:
    calculated_tax = income / 100 * percent
else:
    calculated_tax = 0
string = f'The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!'
print(string)
