try:
    age = int(input("Age: "))
    income = 2000
    risk = income/age
    print(risk)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Invalid age")