import random 
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.conf import settings
from .models import User,OneTimePassword
def generateOtp():
    otp=''
    for i in range(6):
        otp=otp+str(random.randint(1,9))
    return otp

def send_otp_to_user(email):
    subject='One time password for email verification'
    otp=generateOtp()
    user=User.objects.get(email=email)
    site_name='Project Syncify'
    body=f'''
    Hi {user.first_name}, Thanks for signing up on {site_name}.
    Please verify your email address with one time password.
    Your otp is : {otp}
    '''
    OneTimePassword.objects.create(user=user,code=otp)
    email = EmailMultiAlternatives(subject , '', to=[email])
    email.attach_alternative(body, "text/html")
    email.send(fail_silently=True)
    
def send_email_to_user(data):
    email = EmailMultiAlternatives(data['email_subject'] , '', to=[data['to_email']])
    email.attach_alternative(data['email_body'], "text/html")
    email.send(fail_silently=True)
    