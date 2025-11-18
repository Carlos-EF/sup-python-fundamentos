from typing import List
import questionary
from rich.table import Table
from rich.console import Console
import os
import platform


Console = Console()


class Player:
    def __init__(self, nick: str):
        self.nick = nick
        self.vida = 100
        self.stamina = 100

    def ataque(self, adversario: "Player"):
        print(self.nick, "ataque básico", adversario.nick)
        self.stamina = self.stamina - 5
        adversario.vida = adversario.vida - 2

    def ataque_escada(self, adversario: "Player"):
        print(self.nick, "ataque escada", adversario.nick)
        self.stamina = self.stamina - 2
        adversario.vida = adversario.vida - 10

    def ult(self, adversario1: "Player", adversario2: "Player"):
        print(self.nick, "ult", adversario1.nick, adversario2.nick)
        self.stamina = self.stamina - 25
        adversario1.vida = adversario1.vida - 30
        adversario2.vida = adversario2.vida - 15


def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def exemplo_player():
    gustavo = Player("gustavo")

    lucas = Player("beneva") 

    felipe = Player("geraldão")

    game_over = False
    players = [gustavo, lucas, felipe]
    indice_player_atual = 0

    choices = [
        questionary.Choice(gustavo.nick, gustavo),
        questionary.Choice(lucas.nick, lucas),
        questionary.Choice(felipe.nick, felipe)
    ]

    while game_over == False:
        player_atual = players[indice_player_atual]
        limpar_tela()

        ataque = questionary.select(
            f"{player_atual.nick} escolha seu ataque:",
            choices=["Básico", "Escada", "ULT", "Nenhum"]
        ).ask()

        if ataque == "ULT":
            adversarios = questionary.checkbox(
                "Escolhas seus adversários:",
                choices=choices
            ).ask()
            player_atual.ult(adversario1=adversarios[0], adversario2=adversarios[1])
        elif ataque == "Básico":
            adversario = questionary.select(
                "Escolha seu adversário:",
                choices=choices
            ).ask()
            player_atual.ataque(adversario)
        elif ataque == "Escada":
            adversario = questionary.select(
                "Escolha seu adversário:",
                choices=choices
            ).ask()
            player_atual.ataque_escada(adversario)

        apresentar_dados(lucas, gustavo, felipe)

        for player_verificar_gamer in players:
            if player_verificar_gamer.vida <= 0:
                game_over = True

        indice_player_atual += 1
        if indice_player_atual == len(players):
            indice_player_atual = 0


def apresentar_dados(*players: List[Player]):
    tabela = Table()
    tabela.add_column("Player")
    tabela.add_column("Vida", style="green")
    tabela.add_column("Stamina", style="blue")

    # for convencional
    # for i in range(0, len(player)):
    #     player = players[i]

    # foreach
    for player in players:
        tabela.add_row(player.nick, str(player.vida), str(player.stamina))

    Console.print(tabela)
    input("Aperte ENTER para o próximo round")

