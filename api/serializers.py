from rest_framework import serializers
from kittens.models import Kitten

class KittensSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        fields = '__all__'