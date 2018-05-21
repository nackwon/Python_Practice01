import random

set_list = set([])

for i in range(0, 6):
    random_number = random.randint(1, 45)
    set_list.add(random_number)

print(set_list, sep=', ')