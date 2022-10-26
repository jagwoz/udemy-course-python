import random


def my_generic_function():
    nr = 0
    while True:
        nr = yield nr + random.randint(0, 50)


generator = my_generic_function()

# for i in range(10):
#    print(next(generator))
# print(list(generator))  # all next

next(generator)
# generator.send(None)

print("=")
print(generator.send(500))

