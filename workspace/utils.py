from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_join_request_email(user,workspace):
    token=default_token_generator.make_token(user)
    uid=urlsafe_base64_encode(force_bytes(user.pk))
    activation_link = f"http://127.0.0.1:8000/api/v2/workspace/member/acivate/{uid}/{token}"
    user_email=user.email
    subject = "Join Request for Workspace"
    body=f'''
    Hi {user.first_name}, You have a join request in {workspace}.
    Please accept your join request {activation_link}
    '''

    # Send email
    email = EmailMultiAlternatives(subject , '', to=[user_email])
    email.attach_alternative(body, "text/html")
    email.send(fail_silently=True)

def send_registration_email():
    pass 



def generate_registration_link():
    pass