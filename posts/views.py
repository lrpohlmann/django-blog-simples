from django.shortcuts import render, HttpResponse 
from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count

from .models import PostModel, AssuntoModel, ComentarioModel
from .forms import ComentarioForm


# Create your views here.
def getPaginaHome(request):
    posts = PostModel.objects.all().order_by('-data_criacao').annotate(Count('comentariomodel'))
    paginator = Paginator(posts, 6)

    page = request.GET.get('page')
    if page:
        page_obj = paginator.get_page(page)
    else:
        page_obj = paginator.get_page(1)
    
    return render(request, 'home.html', context={
        'posts': page_obj
    })

def getPaginaDePostEspecifico(request, post_id):
    post = PostModel.objects.annotate(Count('comentariomodel')).get(pk=post_id)
    comentarios = ComentarioModel.objects.filter(post=post)

    if request.method == 'GET':
        comentario_form = ComentarioForm(initial={'post': post_id})
    elif request.method == 'POST' and request.user.is_authenticated:
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.autor = request.user
            comentario.save()

    return render(request, 'post_especifico.html', context={
        'post': post,
        'comentarios': comentarios,
        'comentario_form': comentario_form
    })

def getPaginaDePostsDeUmAssunto(request, assunto):
    posts = PostModel.objects.filter(assunto__assunto=assunto)
    return render(request, 'posts_assunto.html', context={
        'posts': posts,
        'assunto': assunto
    })

def getAssuntosJSON(request):
    if request.method == 'GET':
        query_set_assuntos = AssuntoModel.objects.all()
        assuntos_json = serializers.serialize('json', query_set_assuntos)
        return HttpResponse(assuntos_json, content_type='application/json')
        