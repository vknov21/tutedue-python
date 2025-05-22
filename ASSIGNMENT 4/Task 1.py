file_name = "sample.txt"

try:
    fp = open(file_name, "r")
except FileNotFoundError:
    print("Error: The file '%s' was not found." % (file_name,))
else:
    line = fp.readline().strip()
    i = 0
    while line != '':
        print("Line %d:" % (i + 1,), line)
        line = fp.readline()
        i += 1
    fp.close()