var1 = int(input("Enter first variable: "))
var2 = int(input("Enter second variable: "))

# swap without third variable
var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2

print("After swapping")
print("var1 =", var1)
print("var2 =", var2)