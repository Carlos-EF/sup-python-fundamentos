from questionary import text, select, confirm
import datetime
import os


def exercicios_dados_produto():

    pedido_produto = ""

    nome_produto : str =  text("Digite o nome do produto").ask()

    categorias = ["Esportes", "Roupas Esportivas", "Calçados", "Acessórios", "Equipamentos", "Suplementos e Nutrição", "Marcas", "Ofertas e Categorias Especiais"]

    categoria_produto : str = select("Selecione a categoria do produto", choices=categorias).ask()

    data_vencimento_produto : str = text("Digite a data de vencimento do produto no formato: dd-mm-aaaa").ask()

    data_vencimento_formatada = datetime.datetime.strptime(data_vencimento_produto, '%d-%m-%Y').date().strftime('%d-%m-%Y')

    dia_vencimento = data_vencimento_formatada.split("-")[0]

    mes_vencimento = data_vencimento_formatada.split("-")[1]

    ano_vencimento = data_vencimento_formatada.split("-")[2]

    data_atual = datetime.datetime.now().strftime('%d-%m-%Y')

    dia_atual = data_atual.split("-")[0]

    mes_atual = data_atual.split("-")[1]

    ano_atual = data_atual.split("-")[2]

    if mes_vencimento < mes_atual or ano_vencimento < ano_atual:
        print(f"""🛑Produto vencido! Compra não permitida.""")
        return print

    quantidade_produto : int = int(text("DIgite a quantidade que você deseja do produto").ask())

    preco_produto : float = float(text("DIgite o preço do produto").ask().replace("," , "."))

    regioes = ["Sul", "Suldeste", "Centro-Oeste", "Norte", "Nordeste"]

    regiao_entrega : str = select("Selecione a região para a entrega", choices=regioes).ask()

    if regiao_entrega == "Sul":
        valor_frete = 25.00
    elif regiao_entrega == "Suldeste":
        valor_frete = 35.00
    elif regiao_entrega == "Centro-Oeste":
        valor_frete = 45.00
    elif regiao_entrega == "Norte":
        valor_frete = 55.00
    elif regiao_entrega == "Nordeste":
        valor_frete = 50.00

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

    cupom_desconto = confirm("Você possui cupom de desconto?").ask()

    if cupom_desconto == True:
        digitar_cupom_desconto = text("DIgite o cupom de desconto").ask()

        if digitar_cupom_desconto == "SUPER10":
            cupom = "10%"
            desconto_cupom = 1.1
        elif digitar_cupom_desconto == "FRETEGRATIS":
            cupom = "Frete Grátis"
            valor_frete = 0
        elif digitar_cupom_desconto == "PRIME20":
            cupom = "20%"
            desconto_cupom = 1.2
        elif digitar_cupom_desconto == "CLIENTEVIP":
            cupom = "25%"
            desconto_cupom = 1.25
        elif digitar_cupom_desconto == "":
            cupom = "Sem cupom preenchido."
            desconto_cupom = 0
    else:
        cupom = "Sem cupom preenchido."
        desconto_cupom = 0

    valor_do_desconto =  (valor_final_produto * valor_desconto_produto) - valor_final_produto

    valor_final_produto_com_desconto = valor_final_produto - valor_do_desconto

    valor_do_desconto_cupom = 0

    if desconto_cupom != 0:
        valor_do_desconto_cupom = (valor_final_produto_com_desconto * desconto_cupom) - valor_final_produto_com_desconto

        valor_final_produto_com_desconto = valor_final_produto_com_desconto - valor_do_desconto_cupom

    if valor_final_produto_com_desconto > 500.00:
        valor_frete = 0

    valor_final_produto_com_desconto = valor_final_produto_com_desconto + valor_frete

    if dia_atual != dia_vencimento and mes_atual == mes_vencimento:
        valor_final_produto_com_desconto = valor_final_produto_com_desconto - 20
        
        pedido_produto = f"""
        🧾 RESUMO DO PEDIDO
        ------------------------------------
        Produto: {nome_produto}
        Categoria: {categoria_produto}
        Quantidade: {quantidade_produto}
        Preço Unitário: R$ {preco_produto}
        Total Bruto: R$ {valor_final_produto}
        Desconto Categoria ({desconto}): R$ {valor_do_desconto}
        Desconto Cupom: R$ {valor_do_desconto_cupom}
        Frete: R$ {valor_frete}
        ------------------------------------
        Total a Pagar: R$ {valor_final_produto_com_desconto}
        Vencimento: {dia_vencimento}/{mes_vencimento}/{ano_vencimento}
        Região: {regiao_entrega}
        ------------------------------------
        Obrigado por comprar conosco! 
        """

        print(pedido_produto)
        return print

    pedido_produto = f"""
    🧾 RESUMO DO PEDIDO
    ------------------------------------
    Produto: {nome_produto}
    Categoria: {categoria_produto}
    Quantidade: {quantidade_produto}
    Preço Unitário: R$ {preco_produto:.2f}
    Total Bruto: R$ {valor_final_produto:.2f}
    Desconto Categoria ({desconto}): R$ {valor_do_desconto:.2f}
    Desconto Cupom: R$ {valor_do_desconto_cupom}
    Frete: R$ {valor_frete}
    ------------------------------------
    Total a Pagar: R$ {valor_final_produto_com_desconto:.2f}
    Vencimento: {dia_vencimento}/{mes_vencimento}/{ano_vencimento}
    Região: {regiao_entrega}
    ------------------------------------
    Obrigado por comprar conosco! 
    """

    print(pedido_produto)

    gostaria_salvar_pedido_txt = confirm("Gostaria de salvar o pedido?").ask()

    if gostaria_salvar_pedido_txt == True:
        caminho_desktop = os.path.join(os.path.expanduser("~"), "Desktop")

        nome_arquivo = "resumo_pedido.txt"

        caminho_desktop_com_arquivo = os.path.join(caminho_desktop, nome_arquivo)

        with open(caminho_desktop_com_arquivo, "w", encoding="utf-8") as resumo:
            resumo.write(pedido_produto)

        print("Pedido salvo com sucesso no seu Desktop! Obrigado por usar nosso sistema!")
    else:
        print("O pedido não foi salvo. Obrigado por usar o nosso sistema!")