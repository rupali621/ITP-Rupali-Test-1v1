def takingInput():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    operator = input("Enter operator (+,-,*,/): ")
    return number1, number2, operator

def displayResult():
    number1, number2, operator = takingInput()

    if operator == "+":
        result = number1 + number2
        formula = f"{number1} + {number2} = {result}"
    elif operator == "-":
        result = num1 - num2
        formula = f"{number1} - {number2} = {result}"
    elif operator == "*":
        result = number1 * number2
        formula = f"{number1} * {number2} = {result}"
    elif operator == "/":
        result = num1 / num2
        formula = f"{number1} / {number2} = {result}"
    else:
        print("Invalid operator!")
        

    print(formula)

displayResult()
