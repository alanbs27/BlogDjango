from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_cometario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')



    class Meta:
        model = Comentario
        fields = ('nome_cometario', 'email_comentario', 'comentario')