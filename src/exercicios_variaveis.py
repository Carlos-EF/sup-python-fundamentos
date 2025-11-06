from questionary import text, select
import datetime


def exercicios_dados_produto():
    nome_produto : str =  text("Digite o nome do produto").ask()

    categorias = ["Esportes", "Roupas Esportivas", "Calçados", "Acessórios", "Equipamentos", "Suplementos e Nutrição", "Marcas", "Ofertas e Categorias Especiais"]

    categoria_produto : str = select("Selecione a categoria do produto", choices=categorias).ask()

    data_vencimento_produto : str = text("Digite a data de vencimento do produto no formato: dd-mm-aaaa").ask()

    data_vencimento_formatada = datetime.datetime.strptime(data_vencimento_produto, '%d-%m-%Y').date().strftime('%d-%m-%Y')

    dia_vencimento = data_vencimento_formatada.split("-")[0]

    mes_vencimento = data_vencimento_formatada.split("-")[1]

    data_atual = datetime.datetime.now().strftime('%d-%m-%Y')

    dia_atual = data_atual.split("-")[0]

    mes_atual = data_atual.split("-")[1]

    if data_vencimento_formatada < data_atual:
        print(f"""🛑Produto vencido! Compra não permitida.""")
        return print

    quantidade_produto : int = int(text("DIgite a quantidade que você deseja do produto").ask())

    preco_produto : float = float(text("DIgite o preço do produto").ask().replace("," , "."))

    valor_final_produto : float = preco_produto * quantidade_produto

    valor_desconto_produto = 0

    if categoria_produto == "Esportes":
        desconto = "10%"
        valor_desconto_produto = 1.1
        if data_vencimento_formatada == data_atual:
            desconto = f"10% + 70% (vencimento data atual)"
            valor_desconto_produto = 1.8
    elif categoria_produto == "Roupas Esportivas":
        desconto = "15%"
        valor_desconto_produto = 1.15
        if data_vencimento_formatada == data_atual:
            desconto = f"15% + 70% (vencimento data atual)"
            valor_desconto_produto = 1.85
    elif categoria_produto == "Calçados":
        desconto = "20%"
        valor_desconto_produto = 1.2
        if data_vencimento_formatada == data_atual:
            desconto = f"20% + 70% (vencimento data atual)"
            valor_desconto_produto = 1.9
    elif categoria_produto == "Acessórios":
        desconto = "12%"
        valor_desconto_produto = 1.12
        if data_vencimento_formatada == data_atual:
            desconto = f"12% + 70% (vencimento data atual)"
            valor_desconto_produto = 1.82
    elif categoria_produto == "Equipamentos":
        desconto = "8%"
        valor_desconto_produto = 1.08
        if data_vencimento_formatada == data_atual:
            desconto = f"8% + 70% (vencimento data atual)"
            valor_desconto_produto = 1.78
    elif categoria_produto == "Suplementos e Nutrição":
        desconto = "5%"
        valor_desconto_produto = 1.05
        if data_vencimento_formatada == data_atual:
            desconto = f"5% + 70% (vencimento data atual)"
            valor_desconto_produto = 1.75
    elif categoria_produto == "Marcas":
        desconto = "7%"
        valor_desconto_produto = 1.07
        if data_vencimento_formatada == data_atual:
            desconto = f"7% + 70% (vencimento data atual)"
            valor_desconto_produto = 1.77
    elif categoria_produto == "Ofertas e Categorias Especiais":
        desconto = "25%"
        valor_desconto_produto = 1.25
        if data_vencimento_formatada == data_atual:
            desconto = f"25% + 70% (vencimento data atual)"
            valor_desconto_produto = 1.95


    valor_do_desconto =  (valor_final_produto * valor_desconto_produto) - valor_final_produto

    valor_final_produto_com_desconto = valor_final_produto - valor_do_desconto

    if dia_atual != dia_vencimento and mes_atual == mes_vencimento:
        valor_final_produto_com_desconto = valor_final_produto_com_desconto - 20
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
        Valor de desconto extra: R$ 20,00
        Valor final da compra: R$ {valor_final_produto_com_desconto}
        """)
        return print

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