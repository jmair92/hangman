value = float(input())
if value < 2:
    print("Analytic")
elif value >= 2 or value <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")
