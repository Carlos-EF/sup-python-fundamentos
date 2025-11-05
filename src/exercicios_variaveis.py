from questionary import text, select


def exercicios_dados_produto():
    nome_produto : str =  text("Digite o nome do produto").ask()

    categorias = ["Esportes", "Roupas Esportivas", "Calçados", "Acessórios", "Equipamentos", "Suplementos e Nutrição", "Marcas", "Ofertas e Categorias Especiais"]

    categoria_produto : str = select("Selecione a categoria do produto", choices=categorias).ask()

    quantidade_produto : int = int(text("DIgite a quantidade que você deseja do produto").ask())

    preco_produto : float = float(text("DIgite o preço do produto").ask().replace("," , "."))

    valor_final_produto : float = preco_produto * quantidade_produto

    valor_desconto_produto = 0

    if categoria_produto == "Esportes":
        desconto = "10%"
        valor_desconto_produto = 1.1
    elif categoria_produto == "Roupas Esportivas":
        desconto = "15%"
        valor_desconto_produto = 1.15
    elif categoria_produto == "Calçados":
        desconto = "20%"
        valor_desconto_produto = 1.2
    elif categoria_produto == "Acessórios":
        desconto = "12%"
        valor_desconto_produto = 1.12
    elif categoria_produto == "Equipamentos":
        desconto = "8%"
        valor_desconto_produto = 1.08
    elif categoria_produto == "Suplementos e Nutrição":
        desconto = "5%"
        valor_desconto_produto = 1.05
    elif categoria_produto == "Marcas":
        desconto = "7%"
        valor_desconto_produto = 1.07
    elif categoria_produto == "Ofertas e Categorias Especiais":
        desconto = "25%"
        valor_desconto_produto = 1.25

    valor_final_produto_com_desconto = valor_final_produto / valor_desconto_produto

    valor_do_desconto = valor_final_produto - valor_final_produto_com_desconto

    print(f"""
    Dados do pedido:
     -> Produto = {nome_produto}
     -> Categoria do produto = {categoria_produto}
     -> Quantidade = {quantidade_produto}
     -> Preço = R$ {preco_produto}

     Valor da compra: R$ {valor_final_produto}
      _____________________________________
  
     Porcentual do desconto: R$ {desconto}
     Valor do desconto: R$ {valor_do_desconto}
     Valor final da compra: R$ {valor_final_produto_com_desconto}
 """)