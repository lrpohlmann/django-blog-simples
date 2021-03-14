from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import criar_conta, gerenciar_conta, TrocaDePasswordAutenticado


app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('criar_conta/', criar_conta, name='criar_conta'),
    path('gerenciar_conta/', gerenciar_conta, name='gerenciar_conta'),
    path('gerenciar_conta/mudar_senha/', TrocaDePasswordAutenticado.as_view(template_name='mudar_senha.html'), name='mudar_senha')
]