from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "/"
    client_class = OAuth2Client

class GoogleRedirect(APIView):
    def get(self, request):
        return Response("success")

class GoogleLogin(SocialLoginView): # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


def email_confirmation(request, key):
    return redirect(f"http://127.0.0.1:8000/auth/registration/account-confirm-email/{key}")

def reset_password_confirm(request, uid, token):
    return redirect(f"http://127.0.0.1:8000/auth/password/reset/confirm/?{uid}&{token}")