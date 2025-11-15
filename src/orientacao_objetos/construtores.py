from rich.table import Table
from rich.console import Console

class Cachorro:
    # Construtor com 4 parâmetros (3 parâmetros sem valor default e 1 com valor default)
    def __init__(self, raca_param: str, peso: float, idade: int, cor:str = "Caramelo"):
        # Atributos são preenchidos com os dados dos parâmetros
        # O parâmetro cor tem um valor default(padrão) que é "Caramelo"
        self.raca = raca_param
        self.peso = peso
        self.idade = idade
        self.cor = cor
        # self.cor = corAtributo com valor pré-definido
        self.cidade_natal = "Blumenau"


def exemplo_construtor_cachorro():
    # Cahorro(raca, peso, idade)
    tobby = Cachorro("Dobberman", 45.20, 15, "Preto")
    print("raça:", tobby.raca)
    print("peso:", tobby.peso)
    print("idade:", tobby.idade)
    print("cidade natal:", tobby.cidade_natal)
    print("cor:", tobby.cor)

    daschund = Cachorro("Salsicha", 70.00, 5)
    print("raça:", daschund.raca)
    print("peso:", daschund.peso)
    print("idade:", daschund.idade)
    print("cidade natal:", daschund.cidade_natal)
    print("cor:", daschund.cor)


# -------------------------------------------------------------------------------------------
# Exercício de Construtores
# Criar uma classe chamada Passagem com um construtor que contenha os parâmetros abaixo:
# - destino
# - quantidade dias
# - data inicio
# Instanciar dois objetos para desinos diferentes, preenchendo os parâmetros
# Apresentar os dados em uma tabela
# Adicionar os parâmetros abaixo no construtor da classe Passagem
# - quantidade pessoas com valor default 2
# - partida çom valor default 'São Paulo'
# Instanciar outro objeto passando: destino, qtd dias, data inicio, quantidade pessoas
# Apresentar na tabela tbm o novo objeto
# Instanciar outro objeto passando: destino, qtd dias, data inicio, quantidade pessoas, partida
# Apresentar na tabela tbm o novo objeto

class Passagem:
    def __init__(self, destino: str, quantidade_dias: int, data_inicio: str, quantidade_pessoas: int = 2, partida: str = "São Paulo"):
        self.destino = destino
        self.quantidade_dias = quantidade_dias
        self.data_inicio = data_inicio
        self.quantidade_pessoas = quantidade_pessoas
        self.partida = partida


console = Console()

def exercicio_construtor():
    passagem01 = Passagem("Rio de Janeiro", 10, "21/12/2025")
    passagem02 = Passagem("Mato Grosso do Sul", 5, "07/01/2026")

    tabela = Table("Destino", "Quantidade de Dias", "Data de Inicio", "Quantidade de Pessoas" , "Partida", header_style="green", style="blue")
    tabela.add_row(
        passagem01.destino,
        str(passagem01.quantidade_dias),
        passagem01.data_inicio
    )
    tabela.add_row(
        passagem02.destino,
        str(passagem02.quantidade_dias),
        passagem02.data_inicio
    )

    passagem03 = Passagem("Santa Catarina", 2, "07/11/2027", 12)
    passagem04 = Passagem("São Paulo", 7, "27/12/2025", 4, "Santa Catarina")

    tabela.add_row(
        passagem03.destino,
        str(passagem03.quantidade_dias),
        passagem03.data_inicio,
        str(passagem03.quantidade_pessoas)
    )

    tabela.add_row(
        passagem04.destino,
        str(passagem04.quantidade_dias),
        passagem04.data_inicio,
        str(passagem04.quantidade_pessoas),
        passagem04.partida
    )
    console.print(tabela)


exercicio_construtor()