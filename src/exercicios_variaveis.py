from questionary import text


def __solicitar_nome_produto() -> str:
    nome : str = text("Digite o nome do produto").ask()
    return nome


def __solicitar_quantidade_produto() -> int:
    quantidade : int = int(text("DIgite a quantidade que você deseja do produto").ask())
    return quantidade


def __solicitar_preco_produto() -> float:
    preco : float = float(text("DIgite o preço do produto").ask().replace("," , "."))
    return preco


def __solicitar_categoria_produto() -> str:
    categoria = text("Digite a categoria do produto").ask()
    return categoria


def exercicios_dados_produto():
    nome_produto : str = __solicitar_nome_produto()

    categoria_produto : str = __solicitar_categoria_produto()

    quantidade_produto : int = __solicitar_quantidade_produto()

    preco_produto : float = __solicitar_preco_produto()

    valor_final_produto : float = preco_produto * quantidade_produto

    print(f"""
    Dados do pedido:
     -> Produto = {nome_produto}
     -> Categoria do produto = {categoria_produto}
     -> Quantidade = {quantidade_produto}
     -> Preço = R$ {preco_produto}
      _____________________________________

     Valor final da compra: R$ {valor_final_produto}
 """)