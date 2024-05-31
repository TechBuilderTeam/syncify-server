import requests
from google.auth.transport import requests
from google.oauth2 import id_token
from accounts.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed



class Google():
    @staticmethod
    def validate(access_token):
        try:
            id_info=id_token.verify_oauth2_token(access_token, requests.Request())
            if 'accounts.google.com' in id_info['iss']:
                return id_info
        except:
            return "the token is either invalid or has expired"





def register_social_user(provider, email, first_name, last_name,image):
    old_user=User.objects.filter(email=email)
    if old_user.exists():
        if provider == old_user[0].auth_provider:
            register_user=authenticate(email=email, password=settings.SOCIAL_AUTH_PASSWORD)
            tokens=register_user.tokens()
            return {
                'user_id':register_user.id,
                'full_name':register_user.get_full_name,
                'email':register_user.email,
                'tokens':register_user.tokens(),
                "access_token":str(tokens.get('access_token')),
                "refresh_token":str(tokens.get('refresh_token'))
            }
        else:
            raise AuthenticationFailed(
                detail=f"please continue your login with {old_user[0].auth_provider}"
            )
    else:
        new_user={
            'email':email,
            'first_name':first_name,
            'last_name':last_name,
            'image':image,
            'password':settings.SOCIAL_AUTH_PASSWORD
        }
        user=User.objects.create_user(**new_user)
        user.auth_provider=provider
        user.is_verified=True
        user.save()
        login_user=authenticate(email=email, password=settings.SOCIAL_AUTH_PASSWORD)
       
        tokens=login_user.tokens()
        return {
            'user_id':login_user.id,
            'email':login_user.email,
            'full_name':login_user.get_full_name,
            "access_token":str(tokens.get('access_token')),
            "refresh_token":str(tokens.get('refresh_token'))
        }
