def funcao_sem_retorno():
    print("Olá mundo")

def funcao_com_retorno() -> str:
    produto : str = "iPhone 17 Pro Max"
    return produto

def funcao_executar():

    funcao_sem_retorno()

    nome = funcao_com_retorno()
    print("Nome do produto: " + nome)