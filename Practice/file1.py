number1 = float(input("Please enter your first number: "))
number2 = float(input("Please enter your second number: "))

print("Please choose the operation: +,-,*,/")
operation = input("Enter Operation: ")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 != 0:
        result =  number1 / number2
    else:
        result = "Error! Cannot divide by zero"
else:
    result = "Invalid Operation!"
    
print("Result: ", result)