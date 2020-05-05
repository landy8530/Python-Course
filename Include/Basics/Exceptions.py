
try:
    value = 10/0
    number = int(input("Enter a number here: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
