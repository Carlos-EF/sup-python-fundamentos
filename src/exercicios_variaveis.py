from questionary import text, select


def exercicios_dados_produto():
    nome_produto : str =  text("Digite o nome do produto").ask()

    categorias = ["Esportes", "Roupas Esportivas", "Calçados", "Acessórios", "Equipamentos", "Suplementos e Nutrição", "Marcas", "Ofertas e Categorias Especiais"]

    categoria_produto : str = select("Selecione a categoria do produto", choices=categorias).ask()

    quantidade_produto : int = int(text("DIgite a quantidade que você deseja do produto").ask())

    preco_produto : float = float(text("DIgite o preço do produto").ask().replace("," , "."))

    valor_final_produto : float = preco_produto * quantidade_produto

    desconto_produto : float = 0.00

    if categoria_produto == "Esportes":
        desconto_produto = 10.00
        valor_final_produto_com_desconto = valor_final_produto - desconto_produto
    elif categoria_produto == "Roupas Esportivas":
        desconto_produto = 15.00
        valor_final_produto_com_desconto = valor_final_produto - desconto_produto
    elif categoria_produto == "Calçados":
        desconto_produto = 20.00
        valor_final_produto_com_desconto = valor_final_produto - desconto_produto
    elif categoria_produto == "Acessórios":
        desconto_produto = 12.00
        valor_final_produto_com_desconto = valor_final_produto - desconto_produto
    elif categoria_produto == "Equipamentos":
        desconto_produto = 8.00
        valor_final_produto_com_desconto = valor_final_produto - desconto_produto
    elif categoria_produto == "Suplementos e Nutrição":
        desconto_produto = 5.00
        valor_final_produto_com_desconto = valor_final_produto - desconto_produto
    elif categoria_produto == "Marcas":
        desconto_produto = 7.00
        valor_final_produto_com_desconto = valor_final_produto - desconto_produto
    elif categoria_produto == "Ofertas e Categorias Especiais":
        desconto_produto = 25.00
        valor_final_produto_com_desconto = valor_final_produto - desconto_produto

    print(f"""
    Dados do pedido:
     -> Produto = {nome_produto}
     -> Categoria do produto = {categoria_produto}
     -> Quantidade = {quantidade_produto}
     -> Preço = R$ {preco_produto}

     Valor da compra: R$ {valor_final_produto}
      _____________________________________
  
     Valor do desconto: R$ {desconto_produto}
     Valor final da compra: R$ {valor_final_produto_com_desconto}
 """)