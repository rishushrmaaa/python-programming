base = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

result = 1
count = 0

while count < power:
    result = result * base
    count += 1

print(f"{base} to the power of {power} is {result}")
