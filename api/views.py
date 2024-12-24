
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from kittens.models import Kitten
from .serializers import KittensSerializers

@api_view(['GET'])
def get_kittens(request):
    Kittens = Kitten.objects.all()
    serializer = KittensSerializers(Kittens, many=True)
    return Response(serializer.data)