my_list = ['Car', 'Bag', 'Cup']

for item in my_list:
    print(item)

for number in range(10):
    print(number)

for number in range(10, 6, -1):
    print(number)

# nested loops
for x in range(4):
    for y in range(4):
        print(f'({x},{y})')

# print F
f_string = [5, 5, 2, 5, 2, 2]

for count in f_string:
    print('*' * count)

print(f_string[0:4])

# finding maximum number
numbers_list = [10, 15, 12, 56, 23, 9, 6, 54]
print(max(numbers_list))

max_num = numbers_list[0]
number: int  # type hint

for number in numbers_list:
    if max_num < number:
        max_num = number

print(max_num)
numbers_list.sort()
print(numbers_list[-1])

numbers_list.append(67)
print(f'append 67: {numbers_list}')

numbers_list.insert(3, 53)
print(f'insert 53 at index 3: {numbers_list}')

numbers_list.remove(23)
print(f'remove 23: {numbers_list}')

print(f'pop : {numbers_list.pop()}')
numbers_list.clear()
print(f'after clear: {numbers_list}')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()

