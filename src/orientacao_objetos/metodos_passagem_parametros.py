from typing import List
from rich.table import Table
from rich.console import Console

class Aluno:
    def __init__(
            self,
            nome:str,
            notas: List[float],
            frequencia: float = 75,
            turma:str = "SuperDev"
            ):
            self.nome = nome
            self.notas = notas
            self.frequencia = frequencia
            self.turma = turma


def exemplo_passagem_parametros_nomeado():
    pedro = Aluno(
         "Pedro Silva",
         [8, 7, 6.5],
         turma="SuperDev 7°"
    )

    maria = Aluno(
         notas=[10, 9.75, 3],
         nome="Maria",
         turma="Adas",
         frequencia=100
    )

# ------------------------------------------------------------------------------
# Exercício de métodos com parâmetros nomeados
# Criar uma classe chamada Player com os seguintes parâmetros no construtor
# nick com valor default "Geraldão"
# classe com valor default "tanque"
# lane com valor default "meio"
# elo com valor default "bronze"
# maestria com valor default "7"
# main com valor default "Jinx"
# N utilizar os mesmos atributos, mudar a cada instancia nova (utilizar outros)
# Instanciar um objeto com 3 atributos noemados
# Instanciar um objeto com 2 atributos noemados
# Instanciar um objeto com 1 atributo noemado
# Instanciar um objeto com 5 atributos noemados
# Instanciar um objeto com 4 atributos noemados
# Instanciar um objeto com 6 atributos noemados
# Instanciar um objeto com 2 atributos noemados
# Apresentar os dados
# 
# Ex 2: Criar uma classe com 4 parâmetros alguns com valores defaults e outros n
# Instanciar objetos e apresentar
# 
# Ex 3: Criar uma classe com 10 parâmetros alguns com valores defaults 
# e outros n
# Instanciar objetos e apresentar

console = Console()

class Player:
     def __init__(
               self,
               nick:str = "Geraldão",
               classe:str = "Tanque",
               lane:str = "Meio",
               elo:str = "Bronze",
               maestria:str = "7",
               main:str = "Jinx",
               ):
          self.nick = nick
          self.classe = classe
          self.lane = lane
          self.elo = elo
          self.maestria = maestria
          self.main = main


def criar_players():
     players: List[Player] = []

     player_01 = Player(
          nick="Pedrinhogameplays",
          lane="Selva",
          main="Shaco"
     )

     player_02 = Player(
          elo="Diamante",
          maestria="4"
     )

     player_03 = Player(
          classe="Mago"
     )

     player_04 = Player(
          nick="João de Barro",
          classe="Assassino",
          lane="Suporte",
          elo="Mestre",
          main="Pyke"
     )

     player_05 = Player(
          maestria="5",
          main="Sivir",
          lane="Atirador",
          elo="Ferro"
     )

     player_06 = Player(
          nick="Faker do Sul",
          classe="Mago",
          lane="Topo",
          elo="Desafiante",
          maestria="9",
          main="Syndra"
     )

     player_07 = Player(
          main="Graves",
          lane="Selva"
     )

     players.append(
          player_01
     )
     players.append(
          player_02
     )
     players.append(
          player_03
     )
     players.append(
          player_04
     )
     players.append(
          player_05
     )
     players.append(
          player_06
     )
     players.append(
          player_07
     )

     tabela = Table(
          "Nickname",
          "Classe",
          "Lane",
          "Elo",
          "Maestria",
          "Main",
     )

     for i in range(0, len(players)):
          player = players[i]

          tabela.add_row(
               player.nick,
               player.classe,
               player.lane,
               player.elo,
               player.maestria,
               player.main,
          )
     
     console.print(tabela)


class Pokemon:
     def __init__(
               self,
               nome: str,
               tipo_primario: str,
               tipo_secundario: str = "Nenhum",
               geracao: str = "Primeira"
          ):
          self.nome = nome
          self.tipo_primario = tipo_primario
          self.tipo_secundario = tipo_secundario
          self.geracao = geracao


def criar_pokemons():
     pokemons : List[Pokemon] = []

     pikachu = Pokemon(
          nome="Pikachu",
          tipo_primario="Elétrico",
     )

     absol = Pokemon(
          nome="Absol",
          tipo_primario="Sombrio",
          geracao="Terceira"
     )

     pokemons.append(pikachu)
     pokemons.append(absol)

     tabela = Table("Nome", "Tipos", "Geração")

     for i in range(0, len(pokemons)):
          pokemon = pokemons[i]

          tabela.add_row(
               pokemon.nome,
               f"{pokemon.tipo_primario}/{pokemon.tipo_secundario}",
               pokemon.geracao
          )

     console.print(tabela)


class Empresa:
     def __init__(
               self,
               nome_empresa: str,
               cnpj: str,
               data_inauguracao: str,
               faturamento: float,
               socio: str,
               tipo_comercio: str = "Vendas",
               produto_principal: str = "Refrigerantes",
               pais_origem: str = "Brasil",
               situacao_cadastro: str = "Ativa",
               telefone_matriz: str = "(47) 4002-8922"
               ):
          self.nome_empresa = nome_empresa
          self.cnpj = cnpj
          self.data_inauguracao = data_inauguracao
          self.faturamento = faturamento
          self.socio = socio
          self.tipo_comercio = tipo_comercio
          self.produto_principal = produto_principal
          self.pais_origem = pais_origem
          self.situacao_cadastro = situacao_cadastro
          self.telefone_matriz = telefone_matriz


def criar_empresas():
     empresas: List[Empresa] = []

     technova = Empresa(
          nome_empresa= "TechNova Sistemas Ltda",
          cnpj= "12.345.678/0001-90",
          data_inauguracao= "21/08/2015",
          faturamento= 1250000.75,
          socio= "Marcos Andrade",
          tipo_comercio= "Tecnologia",
          produto_principal= "Placa de Vídeo",
          telefone_matriz= "(11) 4002-8922"
     )

     greenagro = Empresa(
          nome_empresa= "GreenAgro Export Ltd.",
          cnpj= "45.987.123/0001-55",
          data_inauguracao= "05/11/2001",
          faturamento= 78000000.30,
          socio=  "José Carvalho",
          tipo_comercio= "Agroindústria",
          produto_principal= "Soja Exportação",
     )

     nordicola = Empresa(
          nome_empresa= "NordiCola Ltda",
          cnpj= "77.222.444/0001-88",
          data_inauguracao= "30/06/2012",
          faturamento= 4300000.50,
          socio= "Erik Johansen",
     )

     empresas.append(technova)
     empresas.append(greenagro)
     empresas.append(nordicola)

     tabela = Table(
          "Nome",
          "CNPJ",
          "Data de Inauguração",
          "Faturamento",
          "Sócio",
          "Tipo de Comércio",
          "Produto Príncipal",
          "País de Origem",
          "Situação",
          "Telefone Matriz",
          )

     for i in range(0, len(empresas)):
          empresa = empresas[i]

          tabela.add_row(
               empresa.nome_empresa,
               empresa.cnpj,
               empresa.data_inauguracao,
               str(empresa.faturamento),
               empresa.socio,
               empresa.tipo_comercio,
               empresa.produto_principal,
               empresa.pais_origem,
               empresa.situacao_cadastro,
               empresa.telefone_matriz,
          )


     console.print(tabela)

