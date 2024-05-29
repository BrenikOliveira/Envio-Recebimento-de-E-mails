#biblioteca utilizada
import smtplib

class EmailSender:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password
        self.smtp_obj = None

    def connect(self):
        try:
            #função contem a conexão ao email e resposta conectado
            self.smtp_obj = smtplib.SMTP_SSL(self.smtp_server, self.port)
            self.smtp_obj.login(self.username, self.password)
            print("Conectado ao servidor SMTP.")
        except Exception as e:
            print(f"Erro ao conectar ao servidor SMTP: {e}")

    def send_email(self, msg_from, msg_subject, msg_body):
        try:
            #confirmação e envio do email ao destinatario 
            msg = f'Subject: {msg_subject}\n{msg_body}'
            self.smtp_obj.sendmail(self.username, msg_from, msg)
            print("Email enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")

    def disconnect(self):
        try:
            # desconectando do email e mensagem de desconectado ao servidor
            self.smtp_obj.quit()
            print("Desconectado do servidor SMTP.")
        except Exception as e:
            print(f"Erro ao desconectar do servidor SMTP: {e}")
            
#iniciação da classe e parametros pre-definidos
if __name__ == "__main__":
    msg_from = input("Informe o e-mail de destino: ")
    smtp_server = 'smtp.gmail.com'
    port = 465
    username = 'brenikarthur@gmail.com'
    password = 'jlix zebv elna nftt'  
    email_sender = EmailSender(smtp_server, port, username, password)
    email_sender.connect()

    msg_subject = 'Titulo do email'
    msg_body = ''
    email_sender.send_email(msg_from, msg_subject, msg_body)
    
    email_sender.disconnect()
