from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class SendMail():
    sender_mail = settings.SENDER_EMAIL 
    
    def __init__(self, temperate, context, subject, to_email):
        self.template = temperate
        self.to_email = to_email
        self.context = context
        self.subject = subject
        
    def  _compose_mail(self):
        html_body = render_to_string(
            self.template,
            self.context
        )

        message = EmailMessage(
            subject=self.subject,
            body=html_body,
            from_email = self.sender_mail,
            to=self.to_email
        )
        message.content_subtype = 'html'
        return message
        
        
    def send(self):
        mail = self._compose_mail()
        mail.send(fail_silently= False)
    