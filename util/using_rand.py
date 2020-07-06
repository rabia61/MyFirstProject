import random

for i in range(3):
    print(random.random())
    print(random.randrange(12, 20))
    print(random.randint(15, 40))

membors = ["John", "Tom", "Jerry"]

print(random.choice(membors))