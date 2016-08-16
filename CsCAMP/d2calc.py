# Simple Calculator
#Branching, Booleans
print("This is a calculator\n+: Addition\n-: Subtraction\n*: Multiplication\n/: Division\n%: Modulus\n**: Exponent\n//: Floor Division")
operation = input("Enter an operator:\n")

a = int(input("Enter Your First Integer:\n"))
b = int(input("Enter Your Second Interger:\n"))

if operation == "+":
    print("Addition: ")
    result = a + b
    print(str(a) + "+" + str(b) + "=" + str(result))
elif operation == "-":
    print("Subtraction:")
    result= a - b
    print(str(a) + "-" + str(b) + "=" + str(result))
elif operation == "*":
    print("Multiplication:")
    result = a * b
    print(str(a) + "*" + str(b) + "=" + str(result))
elif operation == "/":
    print("Divisiom:")
    result= a / b
    print(str(a) + "/" + str(b) + "=" + str(result))
elif operation == "%":
    print("Modulo Operation:")
    result= a % b
    print(str(a) + "%" + str(b) + "=" + str(result))
elif operation == "**":
    print("Exponents:")
    result = a ** b
    print(str(a) + "**" + str(b) + "=" + str(result))
elif operation == "//":
    print("Floor Division:")
    result= a // b
    print(str(a) + "//" + str(b) + "=" + str(result))
else:
    print("Operator not recognized")
