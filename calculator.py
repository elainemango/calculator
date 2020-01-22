num1 = float(input("Enter first number: "))     # include float() so it doesn't convert number input into a string
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "/":
    print (num1 / num2)
elif op == "*":
    print (num1 * num2)
else:
    print ("Invalid operator")
