from django.test import override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.admin import User

from selenium import webdriver
from model_bakery import baker
import shutil
import tempfile

from posts.models import PostModel, AssuntoModel


MEDIA_ROOT = tempfile.mkdtemp()

# falha sempre: ConnectionResetError: [WinError 10054] Foi forçado o cancelamento de uma conexão existente pelo host remoto
'''@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestPaginaHome(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = cls.live_server_url + '/'

        cls.selenium = webdriver.Chrome(executable_path='venv\\ChromeDriver\\bin\\chromedriver.exe')

        user = baker.make(User)
        user.save()

        assunto = baker.make(AssuntoModel)
        assunto.save()

        imagem = SimpleUploadedFile('teste.jpg', content=open('test_utils/media/teste.jpg', 'rb').read(), content_type='image/jpg')

        post = baker.make(PostModel, imagem=imagem)
        post.save()


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_1(self):
        self.selenium.get(self.url)
        post = self.selenium.find_element_by_css_selector('.post-container')
        self.assertTrue(post)
'''