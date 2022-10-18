newList = [
    (1, 'Jacob', 24),
    (2, 'Andrew', 30),
    (3, 'John', 22)
]

for value1, value2, value3 in newList:
    print(value1, value2, value3)

newList2 = [element ** 2 for element in range(20) if element % 3 != 0]
print(newList2)
