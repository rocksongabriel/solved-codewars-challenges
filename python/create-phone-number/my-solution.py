def create_phone_number(n):
    dig1 = "".join(str(v) for v in n[0:3])
    dig2 = "".join(str(v) for v in n[3:6])
    dig3 = "".join(str(v) for v in n[6:10])
    phone_number = f"({dig1}) {dig2}-{dig3}"
    return phone_number

# example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(numbers))