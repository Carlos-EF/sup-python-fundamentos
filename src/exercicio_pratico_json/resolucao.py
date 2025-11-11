from typing import Dict, List
from src.arquivos import ler_json, escrever_json
from rich.console import Console
from rich.table import Table

def resolver():
    # Pegar os dados de algum lugar:
    # - Arquivo => leitura do arquivo
    # - Pegar todos que estão ativos
    #   - Pegar status
    #   - Pegar nome
    #   - Pegar e-mail
    #   - Pegar tipo
    #   - Pegar pontuação
    #   - Adicionar o dado consolidado na lista
    #  - Salvar o arquivo

    # Ler o arquivo e convertendo para uma lsita de dicionário
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    ativos, inativos, suspensos = [], [], []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        conta = usuario.get("conta")
        status = conta.get("status")
        tipo = conta.get("tipo")
        pontuacao = conta.get("pontos")

        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano", "Sem assinatura")

        dados_pessoais = usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")
        email = dados_pessoais.get("email")

        dados = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "pontos": pontuacao,
            "plano": plano,
        }

        if status == "ativo":
            # print(nome, "Ativo")
            ativos.append(dados)
        elif status == "suspenso":
            # print(nome, "Suspenso")
            suspensos.append(dados)
        else:
            # print(nome, "Inativo")
            inativos.append(dados)

    escrever_json(ativos, "data/ativos.json")
    escrever_json(suspensos, "data/suspensos.json")
    escrever_json(inativos, "data/inativos.json")

    apresentar_tabela(ativos, "Contas Ativas")
    apresentar_tabela(inativos, "Contas Inativas")
    apresentar_tabela(suspensos, "Contas Suspensas")


def apresentar_tabela(dados: List[Dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome", header_style="magenta")
    table.add_column("E-Mail", style="blue")
    table.add_column("Tipo", header_style="green")
    table.add_column("Pontuação")
    table.add_column("Plano")

    for i in range(0, len(dados)):
        dado = dados[i]
        table.add_row(
            dado.get("nome"),
            dado.get("email"),
            dado.get("tipo"),
            str(dado.get("pontos")),
            dado.get("plano"),
        )

    console = Console()

    console.print(table)


# Exercício 01
#   Percorrer a lista de usuário, armazenando no arquivo 'free.json' o nome dos usuários que tem o plano Free
def exercicio_01():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    free = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        assinatura = usuario.get("assinatura")

        plano = assinatura.get("plano")

        dados_pessoais = usuario.get("dados_pessoais")

        nome = dados_pessoais.get("nome")

        dados = {
            "nome": nome
        }

        if plano == "Free":
            free.append(dados)
    
    escrever_json(free, "data/free.json")


# Exercício 02
#   Percorrer a lista de usuário, armazenando no arquivo 'tags.json' todas as tags dos usuários
def exercicio_02():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    tags = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]


        tags_usuario = usuario.get("tags")

        for i in range(0, len(tags_usuario)):

         tag = tags_usuario[i]

         tags.append(tag)

    escrever_json(tags, "data/tags.json")




# Exercício 03
#   Percorrer a lista de usuário, armazenando no arquivo 'enderecos.json' todos os endereços dos usuários
# Ex.: ["Rua - Numero - Bairro - CEP - UF", "Rua - Numero - Bairro - CEP - UF"]
def exercicio_03():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    enderecos = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        endereco = usuario.get("endereco")

        rua = endereco.get("rua")

        numero = endereco.get("numero")

        bairro = endereco.get("bairro")

        cep = endereco.get("cep")

        uf = endereco.get("uf")

        dados = {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cep": cep,
            "uf": uf,
        }

        enderecos.append(dados)

    escrever_json(enderecos, "data/enderecos.json")


# Exercício 04:
#   Percorrer a lista de usuários agrupando os dados por estado, salvando o telefone e e-mail de cada usuário em uma lista por estado. Deve armazenar uma lista com os usuários conforme abaixo:
#   Ex.: sc.json
#       [{"email": "elisa.rocha@example.com", "telefone": "......"}]
def exercicio_04():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    mg, sc, rs, pe, sp, ce, ba, am, df, pr, rj = [], [], [], [], [], [], [], [], [], [], []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        dados_pessoais = usuario.get("dados_pessoais")

        email = dados_pessoais.get("email")

        telefone = dados_pessoais.get("telefone")

        endereco = usuario.get("endereco")

        uf = endereco.get("uf")

        dados = {
            "email": email,
            "telefone": telefone
        }

        if uf == "MG":
            mg.append(dados)
        elif uf == "SC":
            sc.append(dados)
        elif uf == "RS":
            rs.append(dados)
        elif uf == "PE":
            pe.append(dados)
        elif uf == "SP":
            sp.append(dados)
        elif uf == "CE":
            ce.append(dados)
        elif uf == "AM":
            am.append(dados)
        elif uf == "DF":
            df.append(dados)
        elif uf == "PR":
            pr.append(dados)
        elif uf == "RJ":
            rj.append(dados)
        elif uf == "BA":
            ba.append(dados)
            

    escrever_json(mg, "data/mg.json")

    escrever_json(sc, "data/sc.json")

    escrever_json(rs, "data/rs.json")

    escrever_json(pe, "data/pe.json")

    escrever_json(sp, "data/sp.json")

    escrever_json(ce, "data/ce.json")

    escrever_json(am, "data/am.json")

    escrever_json(df, "data/df.json")

    escrever_json(pr, "data/pr.json")

    escrever_json(rj, "data/rj.json")

    escrever_json(ba, "data/ba.json")