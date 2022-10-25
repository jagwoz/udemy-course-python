from collections import defaultdict

newDict = {0: '0'}
newDict.update({'0': 0})
print(newDict)

# del(newDict['0'])
# deletedValue = newDict.pop('0')
# deletedValue = newDict.popitem()  # last element

newSet = {0, 2, 3, 1, 6}
print(newSet)
newSet.add(7)

print(newSet & {0, 5, 6})

print(newSet | {0, 5, 6})

print(newSet - {0, 5, 6})

print(newSet ^ {0, 5, 6})

# newSet.discard(0)  # remove element
print({0, 2}.issubset(newSet))

newDefaultDict = defaultdict(float)
newDefaultDict['guest'] += 1.0
print(newDefaultDict)
