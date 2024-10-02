num1 = float(input("Please input your first number: "))
num2 = float(input("Please input your second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 == num2:
    print(f"{num1} and {num2} are equal!")
else:
    print(f"{num2} is greater than {num1}")