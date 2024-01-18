class MathOperations:
    def addition(self, b):
        return self + b

    def soustraction(self, b):
        return self - b

    def multiplication(self, b):
        return self * b

    def division(self, b):
        return self / b

    def puissance(self, b):
        return self ** b

    def modulo(self, b):
        return self % b


def operation(expression):
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
    user_input = input("Tape O pour commencer ou * pour arrêter:")

    if user_input == 'O':
        while True:
            operation_str = input("Entrez votre opération: ")

            if operation_str == '*':
                break

            try:
                result = operation(operation_str)
                print(f"Le résultat de l'opération est: {result}")

            except ValueError as e:
                print(f"Erreur: {e}")


main()
