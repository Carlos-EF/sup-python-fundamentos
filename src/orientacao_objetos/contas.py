import questionary
from rich.console import Console
from rich.table import Table

class Conta:
    def __init__(self, titular: str, saldo_inicial: float):
        """Construtor da classe. Inicializa o títular e o saldo."""
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor_deposito: float):
        """Adiciona um valor ao saldo da conta."""
        if valor_deposito <= 0:
            print(f"DEPÓSITO: Valor de depósito inválido R${valor_deposito:.2f}")
            return

        self.saldo = self.saldo + valor_deposito
        print(f"DEPÓSITO: Depósito de R${valor_deposito:.2f} realizado com sucesso")

    def sacar(self, valor_saque: float):
        """Remove um valor do saldo da conta, se houver dinheiro suficiente."""
        if valor_saque > self.saldo:
            print(f"SAQUE: Saldo insuficiente para realizar o saque de R${valor_saque:.2f}")
        else:
            self.saldo = self.saldo - valor_saque
            print(f"SAQUE: Saque de R${valor_saque:.2f} realizado com sucesso")

    def exibir_saldo(self):
        """Mostrar o status atual da conta."""
        print(f"EXTRATO: Saldo atual de R${self.saldo:.2f}")


def exemplo_conta():
    """Método para testar a funcionalidade da conta"""
    conta_bradesco = Conta("Vitor", 3900.22)

    conta_bradesco.exibir_saldo()
    conta_bradesco.sacar(800) # 3100.22

    conta_bradesco.exibir_saldo()
    conta_bradesco.depositar(100.78) # 3201
    conta_bradesco.depositar(-10)

    conta_bradesco.sacar(4000) # Não permitir pois saldo insuficiente

    conta_bradesco.sacar(3500) # Não permitir pois saldo insuficiente
    conta_bradesco.sacar(3201)
    conta_bradesco.exibir_saldo()


class Aluno:
    def __init__(
            self,
            nome_aluno: str,
            ):
        self.nome = nome_aluno
        self.notas = []


    def adicionar(self):
        nota = "Sim"
        
        while nota == "Sim":
            nota = float(questionary.text(
                "Digite o valor da nota:"
            ).ask().replace(",", "."))

            self.notas.append(nota)

            nota = questionary.select(
                "Deseja adicionar mais notas?",
                choices=["Sim", "Não"]
            ).ask()

    def apresentar_notas(self):
        for nota in self.notas:
            print(f"Nota: {nota}")
    
    def calcular_media(self):
        soma_notas = 0
        for nota in self.notas:
            soma_notas = soma_notas + nota

            media = soma_notas / len(self.notas)

        print(f"Média do aluno {self.nome}: {media:.2f}")


def apresentar_dados_aluno():

    aluno = Aluno("Carlos")

    aluno.adicionar()

    aluno.apresentar_notas()

    aluno.calcular_media()

apresentar_dados_aluno()


    