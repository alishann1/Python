# Odd Numbers

for x in range(1, 101):
    if x % 2 != 0:
        print(x)

# Even numbers

for y in range(1, 101):
    if y % 2 == 0:
        print(y)


# List
list = [1, 2, 3, "myName"]
print(list[1])

# Factorial

integer = int(input("Enter an integer: "))
factorial = 1

# Integer + 1 because the maximum value of "range" doesn't include itself
for i in range(1, integer + 1):
    factorial = factorial * i

print(factorial)

# Find the Factors

number = int(input("Please enter your number: "))
factors = 0

for i in range(1, number + 1):
    if number % i == 0:
        factors += 1
        print("The list of factors of", number, "is ", i)
print("The number of factors of", number, "are ", factors)
