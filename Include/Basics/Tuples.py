
# tuples: immutable data type

coordinates = (4, 5)  # can not modify/change the value

print(coordinates)

print(coordinates[1])

# try to change the value in tuples
# TypeError: 'tuple' object does not support item assignment
# coordinates[1] = 8

coordinates = [(4, 5), (6, 7)]
print(coordinates)