class MathOperations:
    def addition(a, b):
        return a + b
    
    def soustraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("zero ne peut pas etre diviseur")

    def puissance(a, b):
        if a < 0 and isinstance(b, float):
            raise ValueError("ça marche pas, mais j'ai la flm d'expliquer pourquoi")
        else:
            return a ** b
    def modulo(a, b):
        if b != 0:
            return a % b
        else:
            raise ValueError("zero ne peut pas etre diviseur")

def opération(expression):
    parts = expression.split()
    if len(parts) % 2 == 0:
        raise ValueError("Format invalide")

    resultat = float(parts[0])
    for i in range(1, len(parts), 2):
        operateur = parts[i]
        operand = float(parts[i + 1])

        if operateur == '+':
            resultat = MathOperations.addition(resultat, operand)
        elif operateur == '-':
            resultat = MathOperations.soustraction(resultat, operand)
        elif operateur == '*':
            resultat = MathOperations.multiplication(resultat, operand)
        elif operateur == '/':
            resultat = MathOperations.division(resultat, operand)
        elif operateur == '**':
            resultat = MathOperations.puissance(resultat, operand)
        elif operateur == '%':
            resultat = MathOperations.modulo(resultat, operand)
        else:
            raise ValueError(f"Opérateur non supporté: {operateur}")

    return resultat

def main():
    user_input = input("Tape o pour commencer le programme ou * pour l'arrêter:")

    if user_input == 'o':
        while True:
            operation_str = input("Entrez votre opération: ")

            if operation_str == '*':
                break

            try:
                result = opération(operation_str)
                print(f"Le résultat de l'opération est: {result}")

            except ValueError as e:
                print(f"Erreur: {e}")

main()