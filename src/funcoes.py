def funcao_sem_retorno():
    print("Olá mundo")

def funcao_com_retorno() -> str:
    produto : str = "iPhone 17 Pro Max"
    return produto

def funcao_executar():
    funcao_sem_retorno()

    nome = funcao_com_retorno()
    print("Nome do produto: " + nome)




def solicitar_nome_jogo() -> str:
    nome : str = input("Digite o nome do jogo: ").strip()
    return nome

def solicitar_preco_jogo() -> float:
    preco : float = float(input("Digite o preço: "))
    return preco

def solicitar_quantidade_jogo() -> int:
    quantidade : int = int(input("Digite a quantidade: "))
    return quantidade

def solicitar_pedido_fechado() -> bool:
    pedido_fechado : str = input("Pedido fechado (s/n): ").strip().lower()
    if pedido_fechado == "s":
        return True
    else:
        return False

def solicitar_valor_pagamento():
    valor_pagamento : float = float(input("Digite o valor pago: "))
    return valor_pagamento

def processar_pedido():
    nome : str = solicitar_nome_jogo()
    preco : float = solicitar_preco_jogo()
    quantidade : int = solicitar_quantidade_jogo()
    pedido_fechado: bool = solicitar_pedido_fechado()

    valor_pedido : float = quantidade * preco
    print("\n\nValor pedido: " + str(valor_pedido))

    if pedido_fechado == True:
        valor_pagamento = solicitar_valor_pagamento()
        if valor_pagamento > valor_pedido:
            valor_troco = valor_pagamento - valor_pedido
            print("Troco: " + str(valor_troco))
            print("Status: Pedido realizado")
        elif valor_pagamento == valor_pedido:
            print("Pedido sem troco")
            print("Status: Pedido realizado")
        else:
            valor_faltante = valor_pedido - valor_pagamento
            print("Valor faltante: " + str(valor_faltante))
            print("Status: Pedido cancelado")

# ------------------------------------- Exemplo de Cálculo de compra no Paraguai -----------------

def solicitar_cotacao_dolar() -> float:
    cotacao : float = float(input("Digite o valor da cotação do dolar hoje: ").replace(",", "."))
    return cotacao


def solicitar_nome_produto() -> str:
    nome : str = input("DIgite o nome do produto: ")
    return nome


def solicitar_valor_produto_dolar() -> float:
    valor_produto : float = float(input("Digite o valor do produto em dolar: ").replace(",", "."))
    return valor_produto


def solicitar_se_pagara_imposto() -> bool:
    pagara_imposto : str = input("Você pagará imposto? [s/n]: ").lower().strip()
    if pagara_imposto == "s":
        return True
    else:
        return False


def solicitar_deseja_utilizar_cota_dolar_mensal() -> bool:
    return True
    cota_mensal : str = input("Você utilizará a cota mensal? [s/n]: ").lower().strip()
    # if cota_mensal == "s":
    #     return True
    # else:
    #     return False


def calcular_valor_produto_acrescentando_imposto_utilizando_cota(
    valor_produto_dolar : float,
    cotacao_dolar : float,
    valor_produto_reais : float,
):
    cotacao_mensal = 500.00
    # Calcular o valor que será utilizado para descobrir quanro a mais será pago de imposto
    valor_imposto_dolar = (valor_produto_dolar - cotacao_mensal) / 2
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print("Valor total do produto com imposto: " + str(valor_total_produto_reais))


def calcular_valor_produto_acrescentando_imposto(
    valor_produto_dolar : float,
    cotacao_dolar : float,
    valor_produto_reais : float,
):
    valor_imposto_dolar = valor_produto_dolar / 2 #50% de imposto
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print(f"""Valor total do produto: $ {valor_produto_dolar}
    Valor total do produto: R$ {valor_produto_reais}
    Valor imposto: R$ {valor_imposto_reais}
    
    Valor total do produto com imposto: {valor_total_produto_reais}""")


def calcular_valor_compra_paraguai():
    cotacao_dolar : float = solicitar_cotacao_dolar()
    nome_produto : str = solicitar_nome_produto()
    valor_produto_dolar : str = solicitar_valor_produto_dolar()
    pagara_imposto : bool = solicitar_se_pagara_imposto()
    valor_produto_reais = valor_produto_dolar * cotacao_dolar

    if pagara_imposto == True:
        utilizar_cota_dolar_mensal = solicitar_deseja_utilizar_cota_dolar_mensal()

        # Descobrir o valor do produto para calcular o imposto
        if utilizar_cota_dolar_mensal == True:
            calcular_valor_produto_acrescentando_imposto_utilizando_cota(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
        else:
            calcular_valor_produto_acrescentando_imposto(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
    else:
        print("Valor do produto sem pagar imposto: " + str(valor_produto_reais))