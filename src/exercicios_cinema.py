from questionary import text, select

def exercicio_dados_ingresso() :
    nome_filme : str = text("Digite o nome do filme").ask()

    tipos_ingresso = ["Intereira", "Meia"]

    tipo_ingresso : str = select("Qual o tipo do ingresso?", choices=tipos_ingresso).ask()

    quantidade_ingresso : int = int(text("Digite a quantidade de ingressos").ask())

    formatos_sessao = ["2D", "3D", "IMAX"]

    formato_sessao : str = select("Qual o formato da sessão?", choices=formatos_sessao).ask()

    dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

    dia_sessao : str = select("Qual o dia da sessão?", choices=dias_semana).ask()

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
    -> Formato da Sessão: {formato_sessao}
    -> Dia da Sessão: {dia_sessao}
    
    --------------------------------------------------
    
    Valor Final da Compra: R$ {valor_final} """

    print(resumo_pedido_cinema)