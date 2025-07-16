# Calculate factorial of the passed number

def fact(num):
    mul = 1
    for i in range(num, 1, -1):
        mul *= i
    if num < 0:
        print("Input should be a natural number")
    else:
        print(mul)


num = int(input("Enter a number: "))
fact(num)
