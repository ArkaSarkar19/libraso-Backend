from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import BookSerializer, FineSerializer, IssuedSerializer, FineDetailSerializer,complaintSerializer
from .models import Book,  Fine, Issued, complaint
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse





class complaintViewSet(viewsets.ModelViewSet):
    queryset = complaint.objects.all().order_by('title')
    serializer_class = complaintSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('ISBN')
    serializer_class = BookSerializer

    

class FinesViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all().order_by('due_date')
    serializer_class = FineDetailSerializer


class GetFineAPI(generics.GenericAPIView):

    serializer_class = FineSerializer
    def get(self, request, user_id = None,*args, **kwargs):
        if user_id is not None:
            item = Fine.objects.get(user_id = user_id)
            serializer = FineSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            
        item = Fine.objects.all().order_by('due_date')
        serializer = FineSerializer(item)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    


class IssuedViewSet(viewsets.ModelViewSet):
    queryset = Issued.objects.all().order_by('due_date')
    serializer_class = IssuedSerializer


@api_view(['GET', 'POST'])
def issued_books(request,id):
    """
    List all code snippets, or create a new snippet.
    """
    try: 
        tutorial = issued_books.objects.get(pk=id) 
    except issued_books.DoesNotExist: 
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        tutorial_serializer = IssuedSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 


    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    