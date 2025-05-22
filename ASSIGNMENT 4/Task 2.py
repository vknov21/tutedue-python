file_name = "output.txt"

line = input("Enter text to write to the file: ")
fp = open(file_name, "a")
fp.write(line + "\n")
print("Data successfully written to output.txt.")

line = input("Enter additional text to append: ")
fp.write(line + "\n")
print("Data successfully appended.")
fp.close()

fp = open(file_name, "r")

lines = fp.readlines()
print("Final content of the " + file_name + ":")
for line in lines:
    print(line, end='')
fp.close()