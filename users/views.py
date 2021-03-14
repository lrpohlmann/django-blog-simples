from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import UserDescricaoModel

# Create your views here.
def get_pagina_de_lista_de_autores(request):
    autores = UserDescricaoModel.objects.select_related('usuario').filter(e_autor=True).order_by('usuario__first_name')
    return render(request, 'autores.html', context={
        'autores': autores
    })

def criar_conta(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'criar_conta.html', context={
        'form': form
    })

@login_required
def gerenciar_conta(request):
    return render(request, 'gerenciar_conta.html', context={

    })


class TrocaDePasswordAutenticado(LoginRequiredMixin, PasswordChangeView):
    login_url = 'users:login'
    redirect_field_name = 'home'