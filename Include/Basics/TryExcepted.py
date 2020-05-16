# astr = "Hello Bob"
#
# try:
#     istr = int(astr)
# except:
#     istr = -1
#
#
# print("Done" , istr)

rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("Nice work!")
else:
    print("Not a number!")
