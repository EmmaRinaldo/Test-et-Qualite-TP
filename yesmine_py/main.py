def calculer(expression):
    elements = expression.split(' ')
    resultat = float(elements[0])

    i = 1
    while i < len(elements):
        operateur = elements[i]
        suivant = float(elements[i + 1])

        if operateur == '+':
            resultat += suivant
        elif operateur == '-':
            resultat -= suivant
        elif operateur == '*':
            resultat *= suivant
        elif operateur == '/':
            resultat /= suivant
        elif operateur == '%':
            resultat %= suivant
        elif operateur == '^':
            resultat **= suivant
        i += 2

    return resultat

def main():
    while True:
        reponse = input("Souhaitez-vous effectuer un calcul ? (O/*) ")
        if reponse != 'O':
            break

        expression = input("Entrez votre calcul (avec un espace entre chaque élément) : ")
        try:
            resultat = calculer(expression)
            print("Résultat :", resultat)
        except Exception as e:
            print("Erreur de calcul :", e)

if __name__ == "__main__":
    main()

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    @staticmethod
    def modulo(a, b):
        return a % b

def main():
    operations = {
        '+': MathOperations.add,
        '-': MathOperations.subtract,
        '*': MathOperations.multiply,
        '/': MathOperations.divide,
        '^': MathOperations.power,
        '%': MathOperations.modulo
    }

    while True:
        user_input = input("Enter operation (or 'exit' to quit): ")
        if user_input == 'exit':
            break

        try:
            a, op, b = user_input.split()
            a, b = float(a), float(b)
            result = operations[op](a, b)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

