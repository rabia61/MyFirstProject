# tuples are immutable
# they are defined in parenthesis

tuple_num = (1, 2, 3)

# we cannot insert or update but access members by specifying index

print(tuple_num[0])

# unpacking

x, y, z = tuple_num

print(f'x = {x} y = {y} z= {z}')

number_list = [1, 2, 3, 4]

a, b, c, d = number_list

print(f'{a} {b} {c} {d}')