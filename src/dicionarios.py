from typing import Dict, Union


def exemplo_dicionario_basico():
    # Dicionário é uma forma de armazenar chaves e valores
    # Cada chave está atrelado a um valor

    # Dicionário terá uma chave do tipo string
    # Pode armazenar string, int ou bool
    # Criarmos um dicionário com 2 chaves (apelido, idade)
    cachorro: Dict[str, Union[str, int, bool, float]] = {
        "apelido": "Tobby",
        "idade": 4,
        "abandonado": True,
        "peso": 22.5
    }

    # Acrescentar uma nova chave com um valor
    cachorro["raca"] = "Pastor Alemão"

    cachorro["cor"] = "Caramelo"

    # Alterar o valor de uma chave
    cachorro["idade"] = 5

    # Remover uma chave(automaticamente remove o valor)
    cachorro.pop("abandonado")

    # print("Cachorro:", cachorro["apelido"])
    print(f"""
Cachorro: {cachorro.get("apelido")}
Raça: {cachorro.get("raca")}
Idade: {cachorro.get("idade")}
Cor: {cachorro.get("cor")}
Abandonado: {cachorro.get("abandonado")}
Peso: {cachorro.get("peso")}
 """)
    

def exemplo_dicionario_aluno():
    aluno: Dict[str, Union[str, int, float, bool]] = {
        "nome_completo": "John Doe Junior",
        "nome_mae": "Jane Danennet Doe",
        "nome_pai": "John Doe",
        "jogar": True
    }

    print(f"""
Nome do Aluno: {aluno.get("nome_completo")}
Nome da Mãe do Aluno: {aluno.get("nome_mae")}
Nome do Pai do Aluno: {aluno.get("nome_pai")}
Joga? {aluno.get("jogar")}
 """)
    
    aluno["idade"] = 15

    print(f"""
Idade do Aluno: {aluno.get("idade")}
 """)
    
    aluno["idade"] = 16

    aluno.pop("jogar")

    print(f"""
Nome do Aluno: {aluno.get("nome_completo")}
Nome da Mãe do Aluno: {aluno.get("nome_mae")}
Nome do Pai do Aluno: {aluno.get("nome_pai")}
Idade: {aluno.get("idade")}
Joga? {aluno.get("jogar")}
""")