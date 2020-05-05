lucky_numbers = [4, 8, 15, 9, 23, 42]

friends = ["Kevin", "Karen", "Jim", "Jam", "Landy", "Tody"]

friends.append(lucky_numbers)

print(friends)

friends.insert(1, "Kelly")

print(friends)

friends.remove("Jim")

print(friends)

# friends.clear()
# print(friends)

name = friends.pop(1)

print(name)

# index = friends.index("Jim") # 'Jim' is not in list
index = friends.index("Jam")

print(index)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()

print(lucky_numbers)

friends2 = friends.copy()

print(friends2)

