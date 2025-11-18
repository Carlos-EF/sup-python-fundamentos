from enum import Enum
from rich.table import Table
from rich.console import Console

# region Console
class MarcaEnum(Enum):
    SONY = "Sony"
    MICROSOFT = "Microsoft"



class Videogames:
    def __init__(self):
        self.marca : MarcaEnum
        self.modelo : str = ""


def exemplo_consoles():
    # Instanciar um objeto
    play_station = Videogames()
    play_station.marca = MarcaEnum.SONY
    play_station.modelo = "PS1"

    play_station_2 = Videogames()
    play_station_2.marca = MarcaEnum.SONY
    play_station_2.modelo = "PS2"

    xbox = Videogames()
    xbox.modelo = "Xbox"
    xbox.marca = MarcaEnum.MICROSOFT
# endregion



class PessoaTipo(Enum):
    FISICA = "PF"
    JURIDICA = "PJ"


class Pessoa:
    def __init__(self):
        self.nome: str
        self.cpf_cnpj: str
        self.tipo: PessoaTipo


def exemplo_pessoas():
    creber = Pessoa()
    creber.nome = "Cleiton"
    creber.cpf_cnpj = "01.203.200/0001-20"
    creber.tipo = PessoaTipo.FISICA

    print(
        "PESSOA:",
        creber.nome,
        "CPF/CNPJ:",
        creber.cpf_cnpj,
        "TIPO:",
        creber.tipo.value
    )


class PersonagemEnum(Enum):
    BATMAN = "Batman"
    SUPERMAN = "Superman"
    BUZZ_LIGHTYEAR = "Buzz Lightyear"
    HOMEM_FORMIGA = "Homem-Formiga"
    BOB_ESPONJA = "Bob Esponja"
    CATDOG = "CatDog"


class StatusEnum(Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em Andamento"
    CANCELADO = "Cancelado"
    FINALIZADO = "Finalizado"


class Jobs:
    def __init__(self):
        self.personagem = PersonagemEnum
        self.valor: float = 2301.20
        self.local_atuacao: str = "Blumenau"
        self.status = StatusEnum


def criar_jobs():
    job_01 = Jobs()
    job_01.personagem = PersonagemEnum.CATDOG
    job_01.valor = 3000.12
    job_01.local_atuacao = "Gotham City"
    job_01.status = StatusEnum.EM_ANDAMENTO

    job_02 = Jobs()
    job_02.personagem = PersonagemEnum.BUZZ_LIGHTYEAR
    job_02.status = StatusEnum.FINALIZADO

    tabela = Table(
        "Personagem",
        "Valor",
        "Local",
        "Status",
        header_style="green",
        style="blue"
    )

    tabela.add_row(
        job_01.personagem.value,
        str(job_01.valor),
        job_01.local_atuacao,
        job_01.status.value,
    )

    tabela.add_row(
        job_02.personagem.value,
        str(job_02.valor),
        job_02.local_atuacao,
        job_02.status.value,
    )

    console = Console()

    console.print(tabela)
    

criar_jobs()