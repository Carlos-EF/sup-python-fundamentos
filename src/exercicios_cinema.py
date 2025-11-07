from questionary import text, select, confirm

def exercicio_dados_ingresso() :
    nome_filme : str = text("Digite o nome do filme").ask()

    tipos_ingresso = ["Inteiro", "Meia"]

    tipo_ingresso : str = select("Qual o tipo do ingresso?", choices=tipos_ingresso).ask()

    tipo_pessoa = ""

    if tipo_ingresso == "Meia":
        escolha_tipo_pessoa = confirm("Você é estudante?").ask()

        if escolha_tipo_pessoa == True:
            tipo_pessoa = "Estudante"
        else:
            escolha_tipo_pessoa = confirm("Você é idoso?").ask()

            if escolha_tipo_pessoa == True:
                tipo_pessoa = "Idoso"

            else:
                tipo_pessoa = "Nenhum"
    else:
        escolha_tipo_pessoa = confirm("Você é professor?").ask()

        if escolha_tipo_pessoa == True:
            tipo_pessoa = "Professor"
        else:
            tipo_pessoa = "Nenhum"
            

    quantidade_ingresso : int = int(text("Digite a quantidade de ingressos").ask())

    formatos_sessao = ["2D", "3D", "IMAX"]

    formato_sessao : str = select("Qual o formato da sessão?", choices=formatos_sessao).ask()

    dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

    dia_sessao : str = select("Qual o dia da sessão?", choices=dias_semana).ask()

    promo_ingresso_dia = ""

    if dia_sessao == "Qua":
        promo_ingresso_dia = "Quarta do Cinema"
    else:
        promo_ingresso_dia = "Nenhum" 

    preco_ingresso = 0

    desconto_tipo_pessoa = 0

    if tipo_ingresso == "Meia":
        preco_ingresso = 20
    elif tipo_ingresso == "Inteiro": 
        preco_ingresso = 40

    if tipo_pessoa == "Estudante":
        desconto_tipo_pessoa = 5
        preco_ingresso = preco_ingresso - desconto_tipo_pessoa

    if tipo_pessoa == "Idoso":
        desconto_tipo_pessoa = 7
        preco_ingresso = preco_ingresso - desconto_tipo_pessoa

    if tipo_pessoa == "Professor":
        desconto_tipo_pessoa = 4 
        preco_ingresso = preco_ingresso - desconto_tipo_pessoa
    
    if tipo_pessoa == "Nenhum":
        preco_ingresso = preco_ingresso - desconto_tipo_pessoa

    valor_final = preco_ingresso * quantidade_ingresso

    if dia_sessao == "Qua":
        promocao_quarta_cinema = 10
        valor_final = valor_final - promocao_quarta_cinema
    else:
        promocao_quarta_cinema = 0


    resumo_pedido_cinema = f"""
    Resumo do pedido:
    -> Filme: {nome_filme}
    -> Quantidade de ingressos: {quantidade_ingresso}
    -> Tipo do(s) Ingresso(s): {tipo_ingresso}
        -> Desconto Especial por Tipo: {tipo_pessoa}
        -> Valor do Desconto: R$ {desconto_tipo_pessoa:.2f}
    -> Preço Base do(s) Ingresso(s): R$ {preco_ingresso:.2f}
    -> Formato da Sessão: {formato_sessao}
    -> Dia da Sessão: {dia_sessao}
        -> Desconto Especial: {promo_ingresso_dia}
        -> Valor do desconto: R$ {promocao_quarta_cinema:.2f}
    
    --------------------------------------------------
    
    Valor Final da Compra: R$ {valor_final:.2f} """

    print(resumo_pedido_cinema)