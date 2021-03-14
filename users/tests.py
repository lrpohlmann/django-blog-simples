from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.admin import User
from django.contrib.auth import login, logout, authenticate

from model_bakery import baker
import tempfile
import shutil

from .models import UserDescricaoModel

MEDIA_ROOT = tempfile.mkdtemp()

class TestUserDescricao(TestCase):

    def test_criar_descricao(self):
        descricao = baker.make(UserDescricaoModel)
        self.assertIsInstance(descricao, UserDescricaoModel)

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestViewGetDeListaDeAutores(TestCase):

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        imagem = SimpleUploadedFile('teste.jpg', content=open('test_utils/media/teste.jpg', 'rb').read(), content_type='image/jpg')
        self.autores = baker.make(UserDescricaoModel, e_autor=True, imagem=imagem, _quantity=4)
        for autor in self.autores:
            autor.save()

        self.response = self.client.get('/autores/')
        self.status = self.response.status_code
        self.templates = self.response.templates
        self.context = self.response.context
    
    def tearDown(self):
        for autor in self.autores:
            autor.delete()
    
    def test_status(self):
        self.assertTrue(self.status == 200)

    def test_template_name(self):
        self.assertTrue([template.name for template in self.templates if template.name == 'autores.html'])

    def test_context(self):
        self.assertTrue(self.context['autores'])


class TestViewLoginGet(TestCase):

    def setUp(self):
        self.response = self.client.get('/usuarios/login/')
        self.status = self.response.status_code
        self.templates = self.response.templates
        self.context = self.response.context

    def test_status(self):
        self.assertTrue(self.status == 200)

    def test_template_name(self):
        self.assertTrue([template.name for template in self.templates if template.name == 'login.html'])

    def test_context(self):
        pass


class TestViewCriarContaGet(TestCase):

    def setUp(self):
        self.response = self.client.get('/usuarios/criar_conta/')
        self.status = self.response.status_code
        self.templates = self.response.templates
        self.context = self.response.context
    
    def test_status(self):
        self.assertTrue(self.status == 200)

    def test_template_name(self):
        self.assertTrue([template.name for template in self.templates if template.name == 'criar_conta.html'])

    def test_context(self):
        self.assertTrue(self.context['form'])


class TestViewCriarContaPost(TestCase):

    def setUp(self):
        param = {'username': 'usuario1', 'password1': '#>C^aMP~@8', 'password2': '#>C^aMP~@8'}
        self.response = self.client.post('/usuarios/criar_conta/', param)
        self.status = self.response.status_code
        self.templates = self.response.templates
        self.context = self.response.context

    def tearDown(self):
        usuario = User.objects.get(username='usuario1')
        if usuario:
            usuario.delete()

    def test_usuario_criado(self):
        usuario = User.objects.get(username='usuario1')
        self.assertTrue(usuario)


class TestViewGerenciarConta(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user('usuario1', 'mail@mail.com', '#>C^aMP~@8')
        self.usuario.save()
        self.client.login(username='usuario1', password='#>C^aMP~@8')
        if not self.usuario.is_authenticated:
            raise Exception
        
        self.response = self.client.get('/usuarios/gerenciar_conta/')
        self.status = self.response.status_code
        self.templates = self.response.templates
        self.context = self.response.context

    def tearDown(self):
        self.client.logout()
        self.usuario.delete()

    def test_status(self):
        self.assertTrue(self.status == 200)

    def test_template_name(self):
        self.assertTrue([template.name for template in self.templates if template.name == 'gerenciar_conta.html'])


class TestViewMudarSenhaGet(TestCase):

    def setUp(self):
        self.usuario = baker.make(User)
        self.usuario.save()
        
        self.client.force_login(self.usuario)
        if not self.usuario.is_authenticated:
            raise Exception

        self.response = self.client.get('/usuarios/gerenciar_conta/mudar_senha/')
        self.status = self.response.status_code
        self.templates = self.response.templates

    def tearDown(self):
        self.usuario.delete()
        self.client.logout()

    def test_status(self):
        self.assertEqual(self.status, 200)

