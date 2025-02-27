# adapter.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import resolve_url, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        path = ""
        return resolve_url(path)
class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        if not sociallogin.is_existing:
            print(sociallogin.user)
            user = User.objects.create_user(username=sociallogin.user.email, email=sociallogin.user.email)
            user.is_staff = True
            sociallogin.connect(request, user)


