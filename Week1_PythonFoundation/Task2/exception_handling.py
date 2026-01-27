def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+ - * /): ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        else:
            print("Invalid operator")
            return

    except ValueError:
        print("Please enter valid numbers")
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    else:
        print("Result:", result)
    finally:
        print("Calculator finished")

if __name__ == "__main__":
    calculator()
