from questionary import text, select, confirm
import datetime

def exercicio_dados_ingresso() :
    nome_filme : str = text("Digite o nome do filme").ask()

    tipos_ingresso = ["Inteiro", "Meia"]

    tipo_ingresso : str = select("Qual o tipo do ingresso?", choices=tipos_ingresso).ask()

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

    data_sessao : str = text("Digite a data da sessão no formato: dd-mm-aaaa").ask()
   
    data_sessao_formatada = datetime.datetime.strptime(data_sessao, '%d-%m-%Y').date().strftime('%d-%m-%Y')

    dia = data_sessao_formatada.split("-")[0]

    mes = data_sessao_formatada.split("-")[1]

    ano = data_sessao_formatada.split("-")[2]

    data_atual = datetime.datetime.now().date().strftime('%d-%m-%Y')

    dia_atual = data_atual.split("-")[0]

    mes_atual = data_atual.split("-")[1]

    ano_atual = data_atual.split("-")[2]

    if data_sessao_formatada < data_atual:
        print(f"""🛑Sessão inválida! Compra não permitida.""")
        return print

    horario_sessao : str = text("Digite o horário da sessão no formato: hh:mm:ss").ask()

    horario_sessao_formatado = datetime.datetime.strptime(horario_sessao, "%X")

    horario_atual = datetime.datetime.now().time().strftime("%X")

    horas = horario_sessao.split(":")[0]

    minutos = horario_sessao.split(":")[1]

    horas_atual = horario_atual.split(":")[0]

    minutos_atual = horario_atual.split(":")[1]

    if data_sessao_formatada == data_atual:
        if horas < horas_atual and minutos < minutos_atual:
            print(f"""🛑Sessão inválida! Compra não permitida.""")
            return print


    if dia_sessao == "Qua":
        promo_ingresso_dia = "Quarta do Cinema"
    elif dia_sessao == "Sex" or dia_sessao == "Sáb":
        promo_ingresso_dia = "Pico de Demanda (Acréscimo de 10%)"
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

    valor_calculo_ingressos = preco_ingresso * quantidade_ingresso

    valor_final = preco_ingresso * quantidade_ingresso

    if dia_sessao == "Qua":
        taxa = 10
        taxa_calculo_dia_sessao = 10
        valor_final = valor_final - taxa_calculo_dia_sessao
    elif dia_sessao == "Sex" or dia_sessao == "Sáb":
        taxa_calculo_dia_sessao = 1.1
        desconto_dia = (valor_final * taxa_calculo_dia_sessao) - valor_final
        valor_final = valor_final - desconto_dia
        taxa = desconto_dia
    else:
        taxa_calculo_dia_sessao = 0

    if horas <= "16" and minutos <= "59":
        taxa_adicional_horario = "Desconto de 20%"
        desconto_horario = 1.2
        valor_desconto_horario = (valor_final * desconto_horario) - valor_final
    elif horas >= "22":
        taxa_adicional_horario = "Desconto de 10%"
        desconto_horario = 1.1
        valor_desconto_horario = (valor_final * desconto_horario) - valor_final
    else:
        taxa_adicional_horario = "Nenhum"
        valor_desconto_horario = 0

    valor_final = valor_final - valor_desconto_horario


    resumo_pedido_cinema = f"""
    Resumo do pedido:
    -> Filme: {nome_filme}
    -> Quantidade de ingressos: {quantidade_ingresso}
    -> Tipo do(s) Ingresso(s): {tipo_ingresso}
        -> Desconto Especial por Tipo: {tipo_pessoa}
        -> Valor do Desconto: R$ {desconto_tipo_pessoa:.2f}
    -> Preço Base do(s) Ingresso(s): R$ {preco_ingresso:.2f}
    -> Preço Total do(s) Ingresso(s): R$ {valor_calculo_ingressos:.2f}
    -> Formato da Sessão: {formato_sessao}
    -> Dia da Sessão: {dia_sessao}
        -> Taxa Especial: {promo_ingresso_dia}
        -> Valor do desconto: R$ {taxa}
    -> Horário da Sessão: {horario_sessao}
        -> Taxa Adicional: {taxa_adicional_horario}
        -> Valor do Desconto : R$ {valor_desconto_horario:.2f}
    
    --------------------------------------------------
    
    Valor Final da Compra: R$ {valor_final:.2f} """

    print(resumo_pedido_cinema)