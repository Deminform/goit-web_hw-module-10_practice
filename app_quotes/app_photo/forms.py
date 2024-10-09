from django.forms import CharField, FileInput, ImageField, ModelForm, TextInput

from .models import Pictures


class PicturesForm(ModelForm):
    description = CharField(max_length=300, min_length=5,
                            widget=TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}))

    path = ImageField(widget=FileInput(attrs={'class': 'form-control', 'id': 'formFile', 'accept': 'image/*'}))

    class Meta:
        model = Pictures
        fields = ['description', 'path']
