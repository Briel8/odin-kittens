from django.forms import ModelForm
from .models import Kitten

class KittenCreationForm(ModelForm):
    class Meta:
        model = Kitten
        fields = '__all__'