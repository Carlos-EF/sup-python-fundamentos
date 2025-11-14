from datetime import date
import os
import platform
import questionary
from rich.table import Table
from rich.console import Console
from rich.align import Align
from typing import List

class  Endereco:
    def __init__(self):
        self.cidade: str = None
        self.pais: str = None


class Desenvolvedora:
    def __init__(self):
        self.nome: str = None
        self.sede: Endereco = None
        self.proprietario: str = None
        self.jogos: List[Jogo] = []


def limpar_tela():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


        
# Classe é uma representação de objeto do mundo real
class Jogo:
    def __init__(self):
        # atributos da classe
        self.titulo: str = None
        self.data_lancamento: date = None
        self.preco: float = None
        self.genero: str = None
        self.classificacao: str = None
        self.desenvolvedora: Desenvolvedora = None


def exemplo_01():
    # titulo = "GTA VI"
    # data_lancamento = date(2077, 2,28)
    # preco = 650.00
    # genero = "Ação"
    # classificacao = "M"

        # gta_v1_dict = {
        #       "titulo": "GTA VI",
        #       "data_lancamento": date(2077, 2, 28),
        #       "preco": 650.00,
        #       "genero": "Ação",
        #       "classificacao": "M"
        # }


    endereco_rockstar = Endereco()
    endereco_rockstar.cidade = "New York"
    endereco_rockstar.pais = "US"

    rockstar_games = Desenvolvedora()
    rockstar_games.nome = "Rockstar Games"
    rockstar_games.proprietario = "Take-Two Interactive"
    rockstar_games.sede = endereco_rockstar

    #  Instanciando um objeto chamado gta_vi da classe Jogo
    gta_vi = Jogo() #nome_objeto = NomeClasse()
    # Definindo valor para as atributos do objeto
    gta_vi.titulo = "GTA VI"
    gta_vi.data_lancamento = date(2077, 2, 28)
    gta_vi.preco = 650
    gta_vi.genero = "Ação"
    gta_vi.classificacao = "M"
    gta_vi.desenvolvedora = rockstar_games

    gta_vi.preco = 669.99

    the_witcher = Jogo()

    the_witcher.titulo = "The Witcher 4"
    the_witcher.data_lancamento = date(2027, 12, 31)
    the_witcher.preco = 500
    the_witcher.genero = "RPG"
    the_witcher.classificacao = "M"

    league_of_legends = Jogo()

    league_of_legends.titulo = "League of Legends"
    league_of_legends.data_lancamento = date(2009, 10, 27)
    league_of_legends.preco = 0
    league_of_legends.genero = "Moba"
    league_of_legends.classificacao = "12"


    # Adicionar os jogos na desenvolvedora
    rockstar_games.jogos.append(gta_vi)
    rockstar_games.jogos.append(the_witcher)
    rockstar_games.jogos.append(league_of_legends)


    colunas = ["Desenvolvedora", "Título", "Data de Lançamento", "Preço", "Gênero", "Classificação"]
    # Instanciando um objeto chamado tabela da classe Table
    tabela = Table(*colunas)

    tabela.add_row(gta_vi.desenvolvedora.nome, gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificacao)

    tabela.add_row("N/A", the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificacao)

    tabela.add_row("N/A", league_of_legends.titulo, str(league_of_legends.data_lancamento), str(league_of_legends.preco), league_of_legends.genero, league_of_legends.classificacao)

    # Instanciando um objeto chamado console da classe Console
    console = Console()

    console.print(tabela)


class Marca:
    def __init__(self):
        self.id: int = None
        self.nome: str = None
        self.fundador: str = None
        self.data_de_fundacao: date = None
        self.faturamento: float = None


def exercicio_marca():
    amd = Marca()
    amd.id = 1
    amd.nome = "Advanced Micro Devices"
    amd.fundador = "Jerry Sanders"
    amd.data_de_fundacao = date(1969, 7, 1)
    amd.faturamento = 9200000000.00

    intel = Marca()
    intel.id = 2
    intel.nome = "Intel Corporation"
    intel.fundador = "Gordon Moore"
    intel.data_de_fundacao = date(1968, 9, 18)
    intel.faturamento = 53000000000.00

    colunas = ["ID", "Nome", "Fundador", "Data de Fundação", "Faturamento"]
    tabela = Table(*colunas)

    tabela.add_row(str(amd.id), amd.nome, amd.fundador, str(amd.data_de_fundacao), str(amd.faturamento))
    tabela.add_row(str(intel.id), intel.nome, intel.fundador, str(intel.data_de_fundacao), str(intel.faturamento))

    console = Console()
    console.print(tabela)


class Usuario:
    def __init__(self):
        self.id: int = None
        self.nome_completo: str = None
        self.login: str = None
        self.data_nascimento: date = None


class Ticket:
    def __init__(self):
        self.numero: int = None
        self.usuario: Usuario = None
        self.data_abertura: date = None
        self.status: str = None
        self.data_fechamento: date = None
        self.descricao: str = None


def exercicio_ticket():
    usuario01 = Usuario()
    usuario01.id = 1
    usuario01.nome_completo = "John Doe"
    usuario01.login = "johndoe114@hotmail.com"
    usuario01.data_nascimento = date(2003, 12, 1)

    usuario02 = Usuario()
    usuario02.id = 2
    usuario02.nome_completo = "Jane Doe"
    usuario02.login = "janedoe1990@gmail.com"
    usuario02.data_nascimento = date(1990, 1, 1)

    ticket1001 = Ticket()
    ticket1001.numero = 1001
    ticket1001.usuario = usuario01
    ticket1001.data_abertura = date(2025, 11, 12)
    ticket1001.status = "EM ANÁLISE"
    ticket1001.descricao = "Agardando resposta do setor responsável."

    ticket1002 = Ticket()
    ticket1002.numero = 1002
    ticket1002.usuario = usuario01
    ticket1002.data_abertura = date(2025, 11, 2)
    ticket1002.status = "FINALIZADO"
    ticket1002.data_fechamento = date(2025, 11, 12)
    ticket1002.descricao = "Contato realizado/problema resolvido."

    colunas_ticket = ["Número", "Usuario", "Data de Abertura", "Status", "Data de Fechamento", "Descrição"]

    tabela_ticket = Table(*colunas_ticket, title="Tickets")

    tabela_ticket.add_row(str(ticket1001.numero), ticket1001.usuario.nome_completo, str(ticket1001.data_abertura), ticket1001.status, "---- // ----", ticket1001.descricao)
    tabela_ticket.add_row(str(ticket1002.numero), ticket1002.usuario.nome_completo, str(ticket1002.data_abertura), ticket1002.status, str(ticket1002.data_fechamento), ticket1002.descricao)

    colunas_usuario = ["ID", "Nome Completo", "Login", "Data de Nascimento"]

    tabela_usuario = Table(*colunas_usuario, title="Usuários")

    tabela_usuario.add_row(str(usuario01.id), usuario01.nome_completo, usuario01.login, str(usuario01.data_nascimento))
    tabela_usuario.add_row(str(usuario02.id), usuario02.nome_completo, usuario02.login, str(usuario02.data_nascimento))

    console = Console()

    console.print(tabela_ticket, tabela_usuario)


console = Console()
desenvolvedoras : List[Desenvolvedora] = []

def exemplo_crud_lista_objetos():
    menu = ""
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).ask().lower()
        limpar_tela()
        if menu == "adicionar":
            adicionar_desenvolvedora()
        elif menu == "listar":
            listar_desenvolvedoras()


def adicionar_desenvolvedora():
    # Solicitar os dados, instanciando um objeto de desenvolvedora e adicionar na lista
    console.print(Align.center("Cadastro de desenvolvedora"), style="blue")

    desenvolvedora = Desenvolvedora()
    desenvolvedora.nome = questionary.text("Digite o nome da desenvolvedora").ask()
    desenvolvedora.proprietario = questionary.text("Digite o nome do proprietário").ask()

    desenvolvedora.sede = Endereco()
    desenvolvedora.sede.cidade = questionary.text("Digite a cidade da sede").ask()
    desenvolvedora.sede.pais = questionary.text("Digite a país da sede").ask()

    desenvolvedoras.append(desenvolvedora)
    console.print("Desenvolvedora cadastrada com sucesso", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def listar_desenvolvedoras():
    # Listar desenvolvedores
    if len(desenvolvedoras) == 0:
        console.print("Nenhuma desenvolvedora cadastrada", style="red")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        return
    
    table = Table("Nome", "Proprietário", "Endereço")

    for i in range(0, len(desenvolvedoras)):
        desenvolvedora = desenvolvedoras[i]
        table.add_row(
            desenvolvedora.nome,
            desenvolvedora.proprietario,
            f"{desenvolvedora.sede.pais} - {desenvolvedora.sede.cidade}"
        )

    console.print(table)


exemplo_crud_lista_objetos()