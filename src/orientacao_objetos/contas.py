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
    carrinho.adicionar_items("a", 3.0, 1)

    carrinho.exibir_itens()

    # Removendo um item
    carrinho.remover_item("Feijão")
    carrinho.remover_item("Café") # Não existe

    carrinho.exibir_itens()

    # Calculando total
    carrinho.calcular_total()


class AlunoTurma:
    def __init__(self):
        self.nome : str
        self.idade : int
        self.email : str
        self.nota : float

        
class Turma:
    def __init__(self, nome_turma: str):
        self.turma = nome_turma
        self.alunos: List[AlunoTurma] = []

    def listar_alunos(self):
        if len(self.alunos) == 0:
            print(f"Nenhum aluno cadastrado na turma {self.turma}.")
            return

        tabela = Table(
            "Nome",
            "Idade",
            "E-Mail",
            "Nota",
        )

        for aluno in self.alunos:
            tabela.add_row(
                aluno.nome,
                str(aluno.idade),
                aluno.email,
                str(aluno.nota),
                )
        
        console.print(tabela)

    def adicionar_aluno(
            self,
            nome_aluno : str,
            idade : int = 18,
            email : str = "Não informado",
            nota : float = 7.0
        ):
        if nome_aluno == "":
            console.print("ERRO: Nome do aluno não informado!",style="red")
            return
        
        if len(nome_aluno) < 3 or len(nome_aluno) > 50:
            console.print(
                f"ERRO: Nome inválido!",
                style="red"
                )
            return
        
        indice_atual = 0
        for aluno in self.alunos:
            if nome_aluno == aluno.nome:
                console.print(
                    f"ERRO: Aluno já cadastrado!",
                    style="red"
                    )
                return
            indice_atual = indice_atual + 1

        aluno = AlunoTurma()
        aluno.nome = nome_aluno
        aluno.idade = idade
        aluno.email = email
        aluno.nota = nota

        self.alunos.append(aluno)
        console.print(f"Aluno {nome_aluno} cadastrado com sucesso!")
        
    def quantidade_alunos(self):
        quantidade_alunos = len(self.alunos)

        if quantidade_alunos == 0:
            console.print(
                f"AVISO: Nenhum aluno cadastrado na turma {self.turma}.",
                style="red"
                )
            return
            
        console.print(
            f"Quantidade de alunos na turma {self.turma}: {quantidade_alunos}",
            style="blue"
            )
    
    def remover_aluno(self, nome_aluno: str):
        indice_atual = 0
        aluno_removido = False
        for aluno in self.alunos:
            if nome_aluno == aluno.nome:
                aluno_removido = True
                self.alunos.pop(indice_atual)
            indice_atual = indice_atual + 1
        
        if aluno_removido == True:
            console.print(
                f"Aluno {nome_aluno} removido da turma {self.turma}!",
                style="green"
                )
        else:
            console.print(
                f"Aluno {nome_aluno} não faz parte da turma {self.turma}.",
                style="red"
                )


def exemplo_turma():
    turma = Turma("Python Fundamentos")

    turma.listar_alunos()

    # Aluno com todos os dados
    turma.adicionar_aluno(
        "Vitor", 
        idade=20, 
        email="vitor@exemple.com", 
        nota=9.5
        )
    
    # Aluno só com nome e idade
    turma.adicionar_aluno("Ana", idade=18)

    # Aluno só com nome e e-mail
    turma.adicionar_aluno("Marcos", email="marcos@example.com")

    # Aluna só com nome (mínimo de informação)
    turma.adicionar_aluno("Júlia")

    # Tentativa de duplicado
    turma.adicionar_aluno("Vitor") # Duplicado

    turma.listar_alunos()
    turma.quantidade_alunos()

    turma.remover_aluno("Ana")
    turma.remover_aluno("Carlos") # não existe

    turma.listar_alunos()
    turma.quantidade_alunos()

class Contato:
    def __init__(self):
        self.nome : str
        self.telefone : str
        self.email : str

class AgendaContatos:
    def __init__(self):
        self.contatos : List[Contato] = []

    def listar_contatos(self):
        if len(self.contatos) == 0:
            console.print(
                f"ERRO: Nenhum contato cadastrado na agenda.",
                style="red"
                )
            return
        
        tabela = Table(
            "Nome",
            "Telefone",
            "E-Mail",
        )

        for contato in self.contatos:
            tabela.add_row(
                contato.nome,
                contato.telefone,
                contato.email,
            )
        
        console.print(tabela)

    def adicionar_contato(
            self,
            nome_contato : str,
            telefone_contato : str,
            email_contato : str,
            ):
        contato = Contato()
        contato.nome = nome_contato
        contato.telefone = telefone_contato
        contato.email = email_contato
        self.contatos.append(contato)

        console.print(
            f"Contato {nome_contato} adicionado com sucesso!",
            style="green"
            )
    

    def buscar_contato(self, nome_contato : str):
        indice_contato_atual = 0

        nome_contato_encontrado = False

        tabela = Table(
            "Nome",
            "Telefone",
            "E-Mail",
            style="blue"
        )

        for contato in self.contatos:
            if contato.nome == nome_contato:
                tabela.add_row(
                    contato.nome,
                    contato.telefone,
                    contato.email,
                )
                nome_contato_encontrado = True
            indice_contato_atual = indice_contato_atual + 1

        if nome_contato_encontrado == True:
            console.print(tabela)
        else:
            console.print(
                f"ERRO: {nome_contato} não encontrado!",
                style="red")


    def remover_contato(self, nome_contato : str):
        indice_atual_remover = 0

        contato_remover_status = False

        for contato in self.contatos:
            if nome_contato == contato.nome:
                self.contatos.pop(indice_atual_remover)
                contato_remover_status = True
            indice_atual_remover = indice_atual_remover + 1
        
        if contato_remover_status == True:
            console.print(
                f"{nome_contato} removido com sucesso!",
                style="green")
        else:
            console.print(
                f"ERRO: {nome_contato} não encontrado na agenda!",
                style="red")

def exemplo_agenda():
    agenda = AgendaContatos()

    agenda.listar_contatos()
    agenda.adicionar_contato("Ana", "47 99999-0000", "ana@example.com")
    agenda.adicionar_contato("Bruno", "47 98888-1111", "bruno@example.com")
    agenda.adicionar_contato("Ana", "47 97777-2222", "outraana@example.com")

    agenda.listar_contatos()

    agenda.buscar_contato("Bruno")
    agenda.buscar_contato("Carlos")

    agenda.remover_contato("Ana")
    agenda.remover_contato("Carlos")

    agenda.listar_contatos()
