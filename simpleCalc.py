operation = raw_input("Input the math operation you wish to perform (x,+,-,/):")
num1 = raw_input("Input the first number of the maths:")
num2 = raw_input("Input the second number of the maths:")

if operation == "x":
    print(float(num1) * float(num2))
elif operation == "+":
    print(float(num1) + float(num2))
elif operation == "-":
    print(float(num1) - float(num2))
elif operation == "/":
    print(float(num1) / float(num2))
else:
    print("Error.")