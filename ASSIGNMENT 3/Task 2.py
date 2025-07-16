# Prints Square root, Logarithm and Sine value
import math


num = float(input("Enter a number: "))

if num >= 0:
    print("Square root:", math.sqrt(num))
if num > 0:
    print("Logarithm:", math.log(num))
print("Sine:", math.sin(num))
