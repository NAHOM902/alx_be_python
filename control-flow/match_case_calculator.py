num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = num1 + num2
        print(f"The answer is {result}.")
    case "-":
        result = num1 - num2
        print(f"The answer is {result}.")
    case "*":
        result = num1 * num2
        print(f"The answer is {result}.")
    case "/":
        if num2 == 0:
            print("cannot divide by zero.")
        else: 
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. please choose form +, -, *, /.")