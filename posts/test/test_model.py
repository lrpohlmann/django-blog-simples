from django.test import TestCase
from django.contrib.auth.models import User

from model_bakery import baker

from posts.models import PostModel, AssuntoModel, ComentarioModel


class TestAssunto(TestCase):

    def test_criar_assunto(self):
        assunto = AssuntoModel(assunto='python')
        assunto.save()
        self.assertIsInstance(assunto, AssuntoModel)
    
    def test_assunto_str(self):
        assunto = AssuntoModel(assunto='django')
        assunto.save()
        self.assertTrue(str(assunto) == 'django')


class TestPost(TestCase):

    def test_criar_post(self):
        post = baker.make(PostModel)
        self.assertIsInstance(post, PostModel)

    def test_criar_post_com_2_assuntos(self):
        post = baker.make(PostModel, assunto=[])
        post.save()

        assunto = AssuntoModel(assunto='python')
        assunto.save()
        assunto2 = AssuntoModel(assunto='django')
        assunto2.save()

        post.assunto.add(assunto, assunto2)
        self.assertTrue(post.assunto.count() == 2)

    def test_post_str(self):
        user = User(username='user3')
        user.save()

        titulo = 'Eis um titulo'
        post = PostModel(titulo=titulo, corpo='xxxxxxxxxxxxxxxxxxxxxxx', autor=user)
        post.save()

        self.assertTrue(str(post) == titulo)


class TestComentario(TestCase):

    def test_criar_comentario(self):
        comentario = baker.make(ComentarioModel)
        comentario.save()
        self.assertIsInstance(comentario, ComentarioModel)
