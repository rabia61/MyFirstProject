def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Good Morning')


def square(number: int):
    return number * number


print("Start")
# position based argument
greet_user("John", "Smith")

# keyword argument
greet_user(last_name="Marry", first_name="Ferry")
print("Finish")
print(square(67))
