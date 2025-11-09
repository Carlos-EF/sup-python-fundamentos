import requests
from questionary import select, text
from rich.console import Console
from rich.table import Table
from typing import Dict, Union


console = Console()


def mostrar_menu():
    escolha = ""

    while escolha != "Sair":
        escolha = select("Selecione o sistema desejado:",choices=["Funcionarios", "Sistema 2", "Sair"]).ask()

        if escolha == "Funcionarios":
            __mostrar_sistema_funcionarios()


def __mostrar_sistema_funcionarios():
    escolha = ""

    while escolha != "Sair":
        escolha = select("Selecione a função desejada:", choices=["Listar", "Cadastrar", "Editar", "Sair"]).ask()

        if escolha == "Cadastrar":
            __cadastrar_funcionario()
        elif escolha == "Listar":
            __listar_funcionarios()


def __listar_funcionarios():
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")
    tabela.add_column("Cargo")
    tabela.add_column("Salário")
    tabela.add_column("Departamento")
    tabela.add_column("Telefone")

    url = "https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios-detalhes"

    header = {"Content-type": "application/json"}

    response = requests.get(url, headers=header)

    status = response.status_code

    if status == 200:
        conteudo = response.json()

        for funcionario in conteudo:
            id = funcionario["id"]

            nome = funcionario["nome"]

            cargo = funcionario["cargo"]

            departamento = funcionario["departamento"]

            salario = funcionario["salario"]

            telefone = funcionario["telefone"]

            tabela.add_row(str(id), nome, cargo, str(salario), departamento, telefone)
    else:
        print(f"Ocorreu um erro ao tentar carregar os funcionários. Erro: {status}")

    console.print(tabela)


def __cadastrar_funcionario():
    nome_funcionario = text("Digite o nome do funcionario:").ask().strip()

    cargo_funcionario = text("Digite o cargo do funcionario:").ask().strip()

    salario_funcionario = float(text("Digite o salário do funcionario:").ask().replace(",", "."))

    departamento_funcionario = text("Digite o departamento do funcionario:").ask().strip()

    telefone_funcionario = text("Digite o telefone do funcionario:").ask()

    funcionario: Dict[str, Union[str, float]] = {
        "nome": nome_funcionario,
        "cargo": cargo_funcionario,
        "salario": salario_funcionario,
        "departamento": departamento_funcionario,
        "telefone": telefone_funcionario,
    }

    url = "https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios-detalhes"

    header = {"Content-type": "application/json"}

    payload = funcionario

    response = requests.post(url, json=payload, headers=header)

    status = response.status_code

    if status == 201:
        print("Funcionário cadastrado com sucesso!")
    else: 
        print(f"Ocorreu um erro ao tentar cadastrar o funcionário. Erro: {status}")
