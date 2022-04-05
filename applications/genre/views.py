
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from applications.genre.models import Genre
from applications.genre.serializers import GenreSerializer

class ListCreateView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class DeleteUpdateRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

