from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.admin import User
from django.db.models import Count

from model_bakery import baker
import tempfile
import shutil
import json

from posts.models import PostModel, AssuntoModel, ComentarioModel
from posts.views import getPaginaHome


MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestgetPaginaHome(TestCase):

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        imagem = SimpleUploadedFile('teste.jpg', content=open('test_utils/media/teste.jpg', 'rb').read(), content_type='image/jpg')
        self.posts = baker.make(PostModel, imagem=imagem,_quantity=5)
        for post in self.posts:
            post.save()

        self.response = self.client.get('/')
        self.status = self.response.status_code
        self.templates = self.response.templates
        self.context = self.response.context

    def tearDown(self):
        for post in self.posts:
            post.delete()

    def test_status(self):
        self.assertTrue(self.status == 200)

    def test_template_name(self):
        self.assertTrue([template.name for template in self.templates if template.name == 'home.html'])

    def test_context(self):
        self.assertTrue(self.context['posts'])

    def test_post_context(self):
        post = self.context['posts'][0]
        self.assertTrue(hasattr(post, 'comentariomodel__count'))


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestGetPaginaDePostEspecifico(TestCase):

    @classmethod
    def setUpTestData(cls):
        imagem = SimpleUploadedFile('teste.jpg', content=open('test_utils/media/teste.jpg', 'rb').read(), content_type='image/jpg')
        cls.post = baker.make(PostModel, imagem=imagem)
        cls.post.save()

        cls.user = baker.make(User)
        cls.user.save()

        cls.QTD_COMENTARIOS = 5
        cls.comentarios = baker.make(ComentarioModel, post=cls.post, autor=cls.user, _quantity=cls.QTD_COMENTARIOS)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        url = '/posts/{}/'.format(self.post.pk)
        self.response = self.client.get(url)
        self.status = self.response.status_code
        self.templates = self.response.templates
        self.context = self.response.context
    
    def test_status(self):
        self.assertTrue(self.status == 200)

    def test_template_name(self):
        self.assertTrue([template.name for template in self.templates if template.name == 'post_especifico.html'])

    def test_context(self):
        condicoes = all([self.context['post'], self.context['comentarios'], self.context['comentario_form']])
        self.assertTrue(condicoes)

    def test_quantidade_comentarios(self):
        self.assertEqual(self.context['post'].comentariomodel__count, self.QTD_COMENTARIOS)
        

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestGetPaginaDePostEspecificoPost(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        imagem = SimpleUploadedFile('teste.jpg', content=open('test_utils/media/teste.jpg', 'rb').read(), content_type='image/jpg')
        cls.post = baker.make(PostModel, imagem=imagem)
        cls.post.save()

        cls.user = baker.make(User)
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        self.client.force_login(self.user)

        url = '/posts/{}/'.format(self.post.pk)
        dados = {'corpo': 'lorem ipsum', 'post': self.post.pk}
        self.response = self.client.post(url, dados)

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_comentario_realizado(self):
        post_contagem_comentarios = PostModel.objects.annotate(Count('comentariomodel')).get(pk=self.post.pk)
        self.assertEqual(post_contagem_comentarios.comentariomodel__count, 1)