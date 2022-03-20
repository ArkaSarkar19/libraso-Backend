from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer, FineSerializer
from .models import Book,  Fine
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('ISBN')
    serializer_class = BookSerializer

class FinesViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all().order_by('due_date')
    serializer_class = FineSerializer