from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_activation_email(subject,to_email,token):
    message = f"""
    Hello Dear,\n
    The Verification URL For You : http://127.0.0.1:8000/accounts/api/v1/verification/{token}/
    """
    send_mail(subject, message, 'balalzadehhamid79@gmail.com',[to_email], fail_silently=False)

@shared_task
def my_sum(x,y) : return x + y