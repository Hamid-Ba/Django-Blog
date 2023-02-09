from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from mail_templated import EmailMessage
from django.core.mail import send_mail


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


class Email:
    def __init__(self, subject, domain, to_email):
        self.mail_subject = subject
        self.domain = domain
        self.to_email = to_email

    def send_activation_email(self, token):
        # email_obj = EmailMessage(
        #         "activation_email.tpl",
        #         {"token": token},
        #         "balalzadehhamid79@gmail.com",
        #         to=[self.to_email],
        #     )
        # email_obj.send()
        message = f"""
        Hello Dear,\n
        The Verification URL For You : http://127.0.0.1:8000/accounts/api/v1/verification/{token}/
        """
        send_mail(
            self.mail_subject,
            message,
            "balalzadehhamid79@gmail.com",
            [token],
            fail_silently=False,
        )
