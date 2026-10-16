num1 = float(input("Enetr first number: "))
operator = input("Enter any operator (+, -, /, //, *, **, %): ")
num2 = float(input("Enter second number: "))
if operator == "+":
  print("Your answer is", num1 + num2)
elif operator == "-":
  print("Your answer is", num1 - num2)
elif operator == "/":
  if num2 == 0:
    print("Can not divide by zero")
  else:
    print("Your answer is", num1 / num2)
elif operator == "%":
    if num2 == 0:
    print("Cannot divide by zero")
  else:
    print("Your answer is", num1 % num2)
elif operator == "//":
  if num2 == 0:
    print("Cannot divide by zero")
  else:
    print("Your answer is", num1 // num2)
elif operator == "**":
  print("Your answer is", num1 ** num2)
elif operator == "*":
  print("Your answer is", num1 * num2)
else:
  print("Invalid Operator")
