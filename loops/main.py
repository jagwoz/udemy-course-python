x = 0

while x <= 10:
    print(x)
    x += 1


for i in range(0, 10):
    if i % 2 == 0:
        continue
    elif i == 7:
        break
    print(i)

for i in "text":
    print(i)

for i in [0, 2, 5, 11]:
    print(i)
