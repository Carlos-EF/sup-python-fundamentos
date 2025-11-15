from typing import List

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
          pass