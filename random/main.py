import random
from collections import Counter


base = ['green', 'blue', 'purple', 'red', 'orange']

# choices = random.choices(base, [75, 10, 6, 3, 1], k=50)
choices = random.choices(base, [0.75, 0.10, 0.06, 0.03, 0.01], k=50)

random.shuffle(base)
print(base)
print(random.sample(base, 3))

print(Counter(choices))

