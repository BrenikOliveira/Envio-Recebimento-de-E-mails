
#metodo utilizado para os 
import email
#blibioteca para acesso ao protocole de conexão IMAP
import imaplib

class EmailClient:
    def __init__(self, email, password, server):
        self.email = email
        self.password = password
        self.server = server
        #conexão da chave ssl, para criptografar o codigo e deixar a conexão segura
        self.mail = imaplib.IMAP4_SSL(self.server)

    def login(self):
        #solicitação de email e password de conexão ao email, password gerado pelo senha app no gmail
        self.mail.login(self.email, self.password)

    def select_mailbox(self, mailbox):
        #selecionando a caixa de entrada do email
        self.mail.select(mailbox)

    def search_emails(self, criterion='ALL'):
        #pesquisa dentre todos os emails e retorna todos, como é passado no parametro criterion=ALL
        status, data = self.mail.search(None, criterion)
        if status != 'OK':
            raise Exception("Failed to search emails.")
        return data

    def fetch_email(self, email_id):
        #busca pelos email e id, para ver se foi realizada com sucesso
        status, data = self.mail.fetch(email_id, '(RFC822)')
        if status != 'OK':
            raise Exception(f"Failed to fetch email with ID {email_id}.")
        return data

    def process_emails(self, email_ids, specific_person):
        for email_id in email_ids:
            data = self.fetch_email(email_id)
            for response_part in data:
                #verificação se está em um formato de tupla os dados
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    mail_from = message['from']
                    mail_subject = message['subject']
                    mail_content = self.get_mail_content(message)
                    #retorno do email de onde veio, titulo do email e conteudo 
                    if specific_person in mail_from:
                        print(f'From: {mail_from}')
                        print(f'Subject: {mail_subject}')
                        print(f'Content: {mail_content}')

    def get_mail_content(self, message):
        #limpeza dos dados em duas etapas, por meio do texto simples como e repassado em getpayload() ou em multipart() quando ouver a existencia de variados formatos

        if message.is_multipart():
            mail_content = ''
            for part in message.get_payload():
                if part.get_content_type() == 'text/plain':
                    mail_content += part.get_payload()
            return mail_content
        else:
            return message.get_payload()

#iniciando a classe é aqui fica os parametros solicitados na função
if __name__ == "__main__":
    EMAIL = 'brenikarthur@gmail.com'
    PASSWORD = 'jlix zebv elna nftt'
    SERVER = 'imap.gmail.com'
    SPECIFIC_PERSON = ''

    client = EmailClient(EMAIL, PASSWORD, SERVER)
    client.login()
    client.select_mailbox('inbox')  
    data = client.search_emails()
    
    mail_ids = []
    for block in data:
        mail_ids += block.split()
    
    client.process_emails(mail_ids, SPECIFIC_PERSON)
