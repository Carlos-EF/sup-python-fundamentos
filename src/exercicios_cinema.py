from questionary import text, select

def exercicio_dados_ingresso() :
    nome_filme : str = text("Digite o nome do filme").ask()

    tipos_ingresso = ["Intereira", "Meia"]

    tipo_ingresso : str = select("Qual o tipo do ingresso?", choices=tipos_ingresso).ask()

    quantidade_ingresso : int = int(text("Digite a quantidade de ingressos").ask())

    preco_ingresso = 0

    if tipo_ingresso == "Meia":
        preco_ingresso = 20
    else: 
        preco_ingresso = 40

    valor_final = preco_ingresso * quantidade_ingresso

    resumo_pedido_cinema = f"""
    Resumo do pedido:
    -> Filme: {nome_filme}
    -> Quantidade de ingressos: {quantidade_ingresso}
    -> Tipo do(s) Ingresso(s): {tipo_ingresso}
    -> Preço Base do(s) Ingresso(s): R$ {preco_ingresso}
    
    --------------------------------------------------
    
    Valor Final da Compra: R$ {valor_final} """

    print(resumo_pedido_cinema)