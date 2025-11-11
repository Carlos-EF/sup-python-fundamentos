from pathlib import Path
from typing import Dict, List
from json import dumps, load #dumps()
# import json json.dumps()


def escrever_json(data: List, nome_arquivo: str):
    caminho = Path(nome_arquivo).resolve()
    # converte um objeto de Python para uma string JSON
    json_string: str = dumps(data, ensure_ascii=False) # Serialização
    with open(caminho, mode="w", encoding="UTF-8") as arquivo:
        arquivo.write(json_string)
        arquivo.flush()


def ler_json(nome_arquivo : str) -> List | Dict:
    caminho = Path(nome_arquivo).resolve()
    with open(caminho, mode="r", encoding="utf-8") as arquivo:
        dado_deserializado = load(arquivo)
        return dado_deserializado
    

def exemplos_criar_arquivo():
    produtos = [
        {
            "nome": "Abacate",
            "preco": 25.00
        },
        {
            "nome": "Banana",
            "preco": 4.50
        },
        {
            "nome": "Uva",
            "preco": 6.70
        },
    ]
    escrever_json(produtos, "produtos.json")

    games = ["Minecraft", "Roblox", "cs"]
    escrever_json(games, "games.json")

    mine = {
        "nome": "Minecraft",
        "classificacao": 18,
        "preco": 350.00
    }
    escrever_json(mine, "mine.json")


# exemplos_criar_arquivo()


# produtos = ler_json("produtos.json")

# games = ler_json("games.json")

# mine = ler_json("mine.json")

# print(produtos[2].get("nome"))

# print(games[0])

# print(mine.get("nome"))