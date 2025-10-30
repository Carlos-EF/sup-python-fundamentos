def exemplo_strings():
    # Variáveis do tipo string
    nome_inquilino: str = "Maria"
    sobrenome_inquilino : str = "da Silva"

    # Concatenação (junta)
    nome_completo : str = nome_inquilino + " " + sobrenome_inquilino
    print(nome_completo)

# Criar outra função para armazenar os dados do paciente
# nome paciente
# cidade natal
# tipo sanguíneo
# idade
# peso
# altura
# Calcular IMC
# Calcular o ano de nascimento
# apresentar tudo
# Nomenclatura de uma função/método(def) sempre ser uma ação
#  exemplo: apresentar_dados_paciente

def exemplo_int_float():
    salario : int = 1500
    aumento : float = 1.30

    novo_salario : float = salario * aumento

    # str(novo_salario) => converter de float para string
    print("Novo salário: " + str(novo_salario))

def exemplo_boolean():
    # Boolean: True(verdadeiro) ou False(falso)
    empregado: bool = True

    # Alterando o valor da variável empregado
    empregado = False

    print("Empregado: " + str(empregado)) 

def apresentar_dados_paciente():
    nome_paciente: str = "John"
    sobrenome_paciente: str = "Doe"
    cidade_natal: str = "São Paulo"
    tipo_sanquineo: str = "A+"
    idade_paciente: int = 20
    peso_paciente: float = 78.20
    altura_paciente: float = 1.78
    imc_paciente: float = peso_paciente / (altura_paciente * altura_paciente)

    ano_atual : int = 2025

    ano_nascimento_paciente : int = ano_atual - idade_paciente

    nome_paciente_completo: str = nome_paciente + " " + sobrenome_paciente

    print("Dados do paciente: " + 
    "\nNome: " + nome_paciente_completo +
    "\nCidade natal: " + cidade_natal +
    "\nTipo Sanguíneo: " + tipo_sanquineo +
    "\nIdade: " + str(idade_paciente) +
    "\nAno de Nascimento: " + str(ano_nascimento_paciente) +
    "\nPeso: " + str(peso_paciente) +
    "\nAltura: " + str(altura_paciente) +
    "\nIMC " + str(imc_paciente))