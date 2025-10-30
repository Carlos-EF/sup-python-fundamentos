def solicitar_string():
    nome : str = input("Digite o nome: ")
    print("Nome digitado: " + nome)

def solicitar_float():
    nota : float = float(input("Digite a nota: "))
    print("Nota digitada: " + str(nota))

def solicitar_int():
    numero1 : int = int(input("Digite o número 1: "))
    numero2 : int = int(input("Digite o número 2: "))

    soma = numero1 + numero2
    print("Soma: " + str(soma))