from django.test import TestCase
from django.db.models import Count
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

    def setUp(self):
        self.user = User(username='user3')
        self.user.save()

        self.assunto = AssuntoModel(assunto='python')
        self.assunto.save()
        self.assunto2 = AssuntoModel(assunto='django')
        self.assunto2.save()

        self.titulo = 'Eis um titulo'
        self.post = PostModel(titulo=self.titulo, corpo='xxxxxxxxxxxxxxxxxxxxxxx', autor=self.user)
        self.post.save()
        self.post.assunto.add(self.assunto, self.assunto2)
        self.post.save()
        

    def tearDown(self):
        self.post.delete()
        self.user.delete()
        self.assunto.delete()
        self.assunto2.delete()

    def test_criar_post(self):
        self.assertIsInstance(self.post, PostModel)

    def test_criar_post_com_2_assuntos(self):        
        self.assertTrue(self.post.assunto.count() == 2)

    def test_post_str(self):
        self.assertTrue(str(self.post) == self.titulo)

    def test_post_comentario_count(self):
        comentarios = baker.make(ComentarioModel, post=self.post, _quantity=5)
        for comentario in comentarios:
            comentario.save()

        post_com_contagem_de_comentarios = PostModel.objects.annotate(Count('comentariomodel'))[0]

        self.assertEqual(post_com_contagem_de_comentarios.comentariomodel__count, 5)


class TestComentario(TestCase):

    def test_criar_comentario(self):
        comentario = baker.make(ComentarioModel)
        comentario.save()
        self.assertIsInstance(comentario, ComentarioModel)
