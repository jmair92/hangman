cafes = list()
n = list()
while True:
    cafe = input()
    if cafe == "MEOW":
        break
    else:
        cafe = cafe.split(" ")
        cafes.append(cafe[0])
        n.append(int(cafe[1]))
i = n.index(max(n))
print(cafes[i])
