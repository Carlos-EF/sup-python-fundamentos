from src import variaveis
from src import funcoes
from src import conversoes
from src import input_usuario

def main():
    # Exemplos de variáveis
    variaveis.exemplo_strings()
    variaveis.apresentar_dados_paciente()
    variaveis.exemplo_int_float()
    variaveis.exemplo_boolean()

    # Exemplos de funções 
    funcoes.funcao_executar()

    # Exemplos de conversões
    conversoes.converter_str_para_int()
    conversoes.converter_str_para_float()
    conversoes.converter_str_para_boolean()

    # Exemplos de inputs
    input_usuario.solicitar_string()
    input_usuario.solicitar_float()
    input_usuario.solicitar_int()

if __name__ == "__main__":
    main() # executar uma função chamada de main(principal)

# Ctrl + J > py main.py