from typing import List
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

console = Console()

class Produto:
    def __init__(self):
        self.nome: str
        self.preco: float
        self.quantidade: int

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos: List[Produto] = []

    def exibir_itens(self):
        if len(self.produtos) == 0:
            print("Não possui produtos no carrinho.")
            return

        tabela = Table("Nome", "Preço", "Quantidade")

        for produto in self.produtos:
            tabela.add_row(
                produto.nome,
                str(produto.preco),
                str(produto.quantidade),
            )

        console.print(tabela)

    def adicionar_items(
            self,
            nome_produto: str,
            preco_produto: float,
            quantidade_produto: int,
            ):
        if quantidade_produto <= 0:
            console.print("ERRO: Quantidade inválida.")
            return
        
        if preco_produto <= 0:
            console.print("ERRO: Preço inválido.")
            return
        
        if len(nome_produto) < 3 or len(nome_produto) > 50:
            console.print("ERRO: Nome do produto inválido.")
            return

        produto = Produto()
        produto.nome = nome_produto
        produto.preco = preco_produto
        produto.quantidade = quantidade_produto
        self.produtos.append(produto)
        print(f"Produto {nome_produto} adicionado ao carrinho.")
        

    def remover_item(self, nome_produto: str):
        indice = 0

        item_removido = False
        for produto in self.produtos:
            if nome_produto == produto.nome:
                self.produtos.pop(indice)
                item_removido = True
            indice = indice + 1
        
        if item_removido == True:
            print(f"Produto {nome_produto} removido com sucesso")
        else:
            print(f"Produto {nome_produto} não encotrado no carrinho.")

    def calcular_total(self):
        valor_total = 0
        for produto in self.produtos:
            preco = produto.preco
            quantidade = produto.quantidade
            valor_total = valor_total + (preco * quantidade)

        print(f"Valor Total da Compra: R${valor_total:.2f}")

def exemplo_carrinho():
    """Função para testar a funcionalidade do carrinho de compras."""
    carrinho = CarrinhoDeCompras()

    carrinho.exibir_itens()

    carrinho.adicionar_items("Arroz", 25.90, 2)
    carrinho.adicionar_items("Feijão", 8.50, 3)
    carrinho.adicionar_items("Leite", 4.90, 6)

    # Testando casos inválidos
    carrinho.adicionar_items("Chocolate", -10.0, 1)
    carrinho.adicionar_items("Chocolate", 5.0, 0)
    carrinho.adicionar_items("a", 5.0, 1)

    carrinho.exibir_itens()

    # Removendo um item

    carrinho.remover_item("Feijão")
    carrinho.remover_item("Café") # Não existe

    carrinho.exibir_itens()

    # Calculando total
    carrinho.calcular_total()


exemplo_carrinho()