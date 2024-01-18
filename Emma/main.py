# main.py
class MathOperations:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def soustraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is not allowed.")

    @staticmethod
    def evaluate_expression(expression):
        elements = expression.split()
        result = 0
        operator = None

        for element in elements:
            if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
                operand = float(element)
                if operator:
                    result = MathOperations._apply_operator(result, operator, operand)
                else:
                    result = operand
            elif element in ('+', '-', '*', '/'):
                operator = element
            else:
                raise ValueError(f"Invalid element in expression: {element}")

        return result

    @staticmethod
    def _apply_operator(result, operator, operand):
        if operator == '+':
            return MathOperations.addition(result, operand)
        elif operator == '-':
            return MathOperations.soustraction(result, operand)
        elif operator == '*':
            return MathOperations.multiplication(result, operand)
        elif operator == '/':
            return MathOperations.division(result, operand)
        else:
            raise ValueError(f"Invalid operator: {operator}")


print("Bienvenue dans la calculatrice!")

while True:
    user_input = input("Veuillez entrer une expression mathématique (ou 'exit' pour quitter): ")

    if user_input.lower() == 'exit':
        break

    try:
        result = MathOperations.evaluate_expression(user_input)
        print(f"Le résultat est : {result}")
    except ValueError as e:
        print(f"Erreur: {e}")
