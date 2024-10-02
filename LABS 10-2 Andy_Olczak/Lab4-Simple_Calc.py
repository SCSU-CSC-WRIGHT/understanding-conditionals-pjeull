num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
operator = input("Please enter an arithmetic operator (+, -, *, /): ")

# Perform arithmetic operation

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error, cannot divide by zero (0)!"
else:
    result = "Invalid operator!"

print("The result is:", result)