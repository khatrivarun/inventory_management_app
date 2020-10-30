from django.forms import ModelForm, Textarea
from .models import Object


class ObjectForm(ModelForm):
    class Meta:
        model = Object
        fields = ['name', 'quantity', 'description', 'slug']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 10}),
        }
