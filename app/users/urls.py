from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registrar/', views.register_view, name='register'),
    path('menu/', views.menu_view, name='menu'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]