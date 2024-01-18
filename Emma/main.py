# main.py

def calculate(expression):
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '^': lambda x, y: x ** y,
                 '%': lambda x, y: x % y}

    tokens = expression.split()
    result = float(tokens[0])  # Initialize result with the first operand

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = float(tokens[i + 1])
        result = operators[operator](result, operand)

    return result


def main():
    while True:
        user_input = input(
            "Do you want to perform a calculation? (O for yes, * for no): "
        )
        if user_input.lower() != 'o':
            print("Exiting the calculator. Goodbye!")
            break
        expression = input(
            "Enter the calculation (with spaces between each element): "
        )
        try:
            result = calculate(expression)
            print("Result:", result)
        except (ValueError, ZeroDivisionError) as e:
            print("Error:", e)
        another_calculation = input(
            "Do you want to enter another calculation? (O for yes, * for no): "
        )
        if another_calculation.lower() != 'o':
            print("Exiting the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
