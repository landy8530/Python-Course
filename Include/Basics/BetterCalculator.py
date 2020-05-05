

num1 = float(input("Please enter first number: "))

operation = input("Please enter an operator(e.g. + - * /):")

num2 = float(input("Please enter second number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "*":
    print(num1 * num2)
else:
    print("You entering an invalid operation")



