from dotenv import load_dotenv
from os import getenv

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

def __obter_login() -> str:
    email = getenv("EMAIL")
    if email is None:
        raise Exception("Login não está preenchido no aruquivo .env")
    
    return email


def __obter_senha() -> str:
    senha = getenv("SENHA")
    if senha is None:
        raise Exception("Senha não está preenchida no arquivo .env")
    
    return senha


def enviar(destinatario: str, corpo: str):
    mensagem = MIMEMultipart()
    mensagem["From"] = __obter_login()
    mensagem["To"] = destinatario
    mensagem["Subject"] = "Pedido Criado"

    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls() #Criptografia da conexão
            servidor.login(__obter_login(), __obter_senha())
            servidor.send_message(mensagem)
            print("E-mail enviado com sucesso!")
    except Exception as e:
         print("Ocorreu um erro ao tentar enviar o e-mail." + e)


def enviar_email_pedido(destinatario: str, tamanho: str, sabores: list[str]):
    mensagem = f"""Pedido criado com sucesso!
     
      Tamanho da pizza: {tamanho}
      Sabores da pizza: {sabores} 
    """

    enviar(destinatario, mensagem)
