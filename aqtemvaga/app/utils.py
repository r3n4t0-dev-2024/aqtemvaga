from django.core.mail import send_mail
from django.conf import settings

def enviar_email_empregador(email, arquivo_url):
    assunto = 'Novo Currículo Recebido'
    mensagem = f'Você recebeu um novo currículo. Baixe o arquivo aqui: {settings.BASE_URL}{arquivo_url}'
    send_mail(
        assunto,
        mensagem,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
