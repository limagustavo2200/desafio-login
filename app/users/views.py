from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # Verificar se o e-mail existe
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error('email', 'E-mail inexistente')
                return render(request, 'users/login.html', {'form': form})
            
            # Tentar autenticar
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('menu')
            else:
                # Verificar se é um problema de senha
                form.add_error('password', 'Senha inválida')
        
        # Se chegou aqui, teve algum erro de validação
    else:
        form = UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Login automático após registro
            login(request, user)
            return redirect('menu')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def menu_view(request):
    return render(request, 'users/menu.html')