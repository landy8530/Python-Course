def compute_pay(hours, rate):
    print("In compute pay", hours, rate)

    if hours > 40:
        print("Overtime")
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
    else:
        print("Regular")
        reg = hours * rate
        otp = 0.0
    return reg + otp


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
except ValueError:
    print("Errors: name 'sh' is not defined! Please enter numeric input.")
    quit()

try:
    fr = float(sr)
except ValueError:
    print("Errors: name 'sr' is not defined! Please enter numeric input.")
    quit()


payment = compute_pay(fh, fr)

print("Pay", payment)