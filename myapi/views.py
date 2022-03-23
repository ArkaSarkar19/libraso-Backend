from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer, FineSerializer, IssuedSerializer
from .models import Book,  Fine, Issued
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('ISBN')
    serializer_class = BookSerializer

    

class FinesViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all().order_by('due_date')
    serializer_class = FineSerializer

class IssuedViewSet(viewsets.ModelViewSet):
    queryset = Issued.objects.all().order_by('due_date')
    serializer_class = IssuedSerializer


@api_view(['GET', 'POST'])
def issued_books(request,id):
    """
    List all code snippets, or create a new snippet.
    """
    try: 
        tutorial = issued_books.objects.get(pk=pk) 
    except issued_books.DoesNotExist: 
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        tutorial_serializer = IssuedSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    