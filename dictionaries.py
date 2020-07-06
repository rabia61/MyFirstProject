customer = {
    "name" : "John",
    "age" : 42,
    "cpuntry" : "UK"
}

print(customer["name"])
print(customer.get("age"))
print(customer.get("birthdate","January 1, 1990"))

# for emojis press Ctrl + + e and then press space
mappings = {
    ":)": "",
    ":(": ""
}

print(mappings)