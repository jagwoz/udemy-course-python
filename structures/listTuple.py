import copy as cp
from collections import Counter

names = ["Peter", "Oscar"]

names[-1] = "Thom"  # last element
print(names)

if "Thom" in names:  # /not in
    print("Thom is in names")

names = ["Erick"] + names  # .insert(0, "Erick")
names.append("Felix")

names.extend(["John", "Patrick"])

print(names)
print(names.index("Peter"))

names.sort(reverse=True)
print(names)
print(max(names))
print(min(names))

print(names.count("John"))

names.pop()
names.remove("John")
print(names)

names.reverse()
print(names)
# names.clear()


myTuple = "Thom", "Andrew"
my2ndTuple = ("Thom", "Andrew")

list(names)
names[:]
names.copy()  # copy
cp.deepcopy(names)  # deepcopy

new_names = list(filter(lambda x: str(x).startswith("P"), names))
print(new_names)

counter = Counter(names)
print(counter)


