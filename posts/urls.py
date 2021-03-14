from django.urls import path
from django.shortcuts import redirect

from posts.views import getPaginaDePostEspecifico, getPaginaDePostsDeUmAssunto, getAssuntosJSON

app_name = 'posts'

urlpatterns = [
    path('assunto/', lambda x: redirect('home'), name='assunto_root'),
    path('assunto/get/', getAssuntosJSON, name='assuntos_get_json'),
    path('assunto/<str:assunto>', getPaginaDePostsDeUmAssunto, name='posts_assunto'),
    path('<int:post_id>/', getPaginaDePostEspecifico, name='post_especifico'),
]