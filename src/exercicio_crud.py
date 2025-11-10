import requests
from questionary import select, text
from rich.console import Console
from rich.table import Table
from typing import Dict, Union


console = Console()


def mostrar_menu():
    escolha = ""

    while escolha != "Sair":
        escolha = select("Selecione o sistema desejado:",choices=["Funcionarios", "Projetos", "Sair"]).ask()

        if escolha == "Funcionarios":
            __mostrar_sistema_funcionarios()
        elif escolha == "Projetos":
            __mostrar_sistema_projetos()


def __mostrar_sistema_funcionarios():
    escolha = ""

    while escolha != "Sair":
        escolha = select("Selecione a função desejada:", choices=["Listar", "Cadastrar", "Editar", "Apagar", "Sair"]).ask()

        if escolha == "Cadastrar":
            __cadastrar_funcionarios()
        elif escolha == "Listar":
            __listar_funcionarios()
        elif escolha == "Editar":
            __editar_funcionarios()
        elif escolha == "Apagar":
            __apagar_funcionarios()


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


def __cadastrar_funcionarios():
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


def __editar_funcionarios():
    __listar_funcionarios()

    id = text("Digite o ID do funcionário que deseja editar:").ask()

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

    header = {"Content-type": "application/json"}

    payload = funcionario

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios-detalhes/{id}"

    response = requests.put(url, json=payload, headers=header)

    status = response.status_code

    if status == 204:
        print("Funcionário editado com sucesso!")
    elif status == 404:
        print("Funcionário não encontrado.")
    else:
        print(f"Ocorreu um erro ao tentar editar o funcionário. Erro: {status}")


def __apagar_funcionarios():
    __listar_funcionarios()

    id = text("Digite o id do funcionário que deseja apagar:").ask()

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios-detalhes/{id}"
    
    response = requests.delete(url)

    status = response.status_code

    if status == 204:
        print("Funcionário deletado com sucesso!")
    elif status == 404:
        print("Funcionário não encontrado.")
    else:
        print(f"Ocorreu um erro ao tentar apagar o funcionário. Erro: {status}")


# ---------------------------------------------------------------------------------------------------------------------- #


def __mostrar_sistema_projetos():
    escolha = ""

    while escolha != "Sair":
        escolha = select("Selecione a função desejada:", choices=["Listar", "Cadastrar", "Editar", "Apagar", "Sair"]).ask()

        if escolha == "Cadastrar":
            __cadastrar_projetos()
        elif escolha == "Listar":
            __listar_projetos()
        elif escolha == "Editar":
            __editar_projetos()
        elif escolha == "Apagar":
            __apagar_projetos()


def __cadastrar_projetos():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/projetos"

    nome_projeto = text("Digite o nome do projeto:").ask().strip()

    codigo_projeto = text("Digite o código do projeto:").ask().strip()

    custo_projeto = float(text("Digite o custo do projeto:").ask().replace(",", "."))

    projeto: Dict[str, Union[str, float]] = {
        "nome": nome_projeto,
        "codigoProjeto": codigo_projeto,
        "custoEstimado": custo_projeto,
    }

    header = {"Content-type": "application/json"}

    payload = projeto

    response = requests.post(url, headers=header, json=payload)

    status = response.status_code

    if status == 201:
        print("Projeto cadastrado com sucesso!")
    else:
        print(f"Ocorreu um erro ao tentar cadastrar o projeto. Erro: {status}")


def __listar_projetos():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/projetos"

    tabela = Table()
    tabela.add_column("ID")
    tabela.add_column("Nome")
    tabela.add_column("Código Projeto")
    tabela.add_column("Custo Estimado")

    header = {"Content-type": "application/json"}

    response = requests.get(url, headers=header)

    status = response.status_code

    if status == 200:
        conteudo = response.json()

        for projeto in conteudo:
            id = projeto["id"]

            nome = projeto["nome"]

            codigo = projeto["codigoProjeto"]

            custo = projeto["custoEstimado"]

            tabela.add_row(str(id), nome, codigo, str(custo))
        else:
            print(f"Ocorreu um erro ao tentar carregar os projetos cadastrados. Erro: {status}")
    
    console.print(tabela)
        

def __editar_projetos():
    __listar_projetos()

    id = text("Digite o ID do prejeto que deseja editar:").ask()

    nome_projeto = text("Digite o nome do projeto:").ask().strip()

    codigo_projeto = text("Digite o código do projeto:").ask().strip()

    custo_projeto = float(text("Digite o custo do projeto:").ask().replace(",", "."))

    projeto: Dict[str, Union[str, float]] = {
        "nome": nome_projeto,
        "codigoProjeto": codigo_projeto,
        "custoEstimado": custo_projeto,
    }

    payload = projeto

    header = {"Content-type": "application/json"}

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/projetos/{id}"

    response = requests.put(url, headers=header,json=payload)

    status = response.status_code

    if status == 204:
        print("Projeto editado com sucesso!")
    elif status == 404:
        print("Projeto não encontrado.")
    else:
        print(f"Ocorreu um erro ao tentar editar o projeto. Erro: {status}")


def __apagar_projetos():
    __listar_projetos()

    id = text("Digite o ID do prejeto que deseja apagar:").ask()

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/projetos/{id}"

    header = {"Content-type": "application/json"}

    response = requests.delete(url, headers=header)

    status = response.status_code

    if status == 204:
        print("Projeto deletado com sucesso!")
    elif status == 404:
        print("Projeto não encontrado.")
    else:
        print(f"Ocorreu um erro ao tentar apagar o projeto. Erro: {status}")