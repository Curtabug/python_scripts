equation = 0
num1 = int(input("Please input a number. "))
operator_input = input("Please input an operation. Put the first letter of the operation. ")
operator = 0
num2 = int(input("Please input a second number. "))
answer = 0

if operator_input.upper() == "A":
    operator = "+"
    answer = num1 + num2
elif operator_input.upper() == "S":
    operator = "-"
    answer = num1 - num2
elif operator_input.upper() == "M":
    operator = "*"
    answer = num1 * num2
elif operator_input.upper() == "D":
    operator = "/"
    answer = num1 / num2
elif operator_input.upper() == "E":
    operator = "^"
    answer = num1 ** num2
else:
    print("That is not an operation!")
equation = f"{num1} {operator} {num2}"
print(f"{equation} = {answer}!")
