from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re

class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )

class UserRegisterForm(UserCreationForm):
    # Sobrescrever campos para personalizar
    name = forms.CharField(
        label='Nome',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail'})
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            'id': 'password1'
        })
    )
    password2 = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua senha',
            'id': 'password2'
        })
    )
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', name):
            raise forms.ValidationError('O nome deve conter apenas letras.')
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        # Verificar tamanho mínimo
        if len(password) < 8:
            raise forms.ValidationError('A senha deve ter pelo menos 8 caracteres.')
        
        # Verificar caractere especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError('A senha deve conter pelo menos 1 caractere especial.')
        
        # Verificar número
        if not re.search(r'\d', password):
            raise forms.ValidationError('A senha deve conter pelo menos 1 número.')
        
        # Verificar letra maiúscula
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError('A senha deve conter pelo menos 1 letra maiúscula.')
        
        return password
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não coincidem.')
        
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Usar o email como username
        user.first_name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        
        return user