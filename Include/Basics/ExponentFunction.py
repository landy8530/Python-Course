print(2 ** 3)


def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


print("The result of raise_to_power: " + str(raise_to_power(2, 3)))

