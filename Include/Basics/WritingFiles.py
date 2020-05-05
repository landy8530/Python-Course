
# employee_file = open("../doc/appendingfile.txt", "a") # appending file
# employee_file = open("../doc/writefile.txt", "w") # create a new file
employee_file = open("../doc/index.html", "w") # create a new file

# employee_file.write(" Appending in the end of file")
employee_file.write("<p> This is a html file</p>")

employee_file.close()