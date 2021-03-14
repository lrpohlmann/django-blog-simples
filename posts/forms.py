from django.forms import ModelForm, HiddenInput

from .models import ComentarioModel


class ComentarioForm(ModelForm):

    class Meta:
        model = ComentarioModel
        fields = ['post', 'corpo']
        widgets = {
            'post': HiddenInput()
        }