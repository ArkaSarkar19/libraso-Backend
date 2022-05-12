from datetime import date
import re
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import BookSerializer, EventSerializer, FineSerializer, IssuedSerializer, complaintSerializer, EventSerializer
from .models import Book,  Fine, Issued, complaint, Event
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.http.response import JsonResponse





class complaintViewSet(viewsets.ModelViewSet):
    queryset = complaint.objects.all().order_by('title')
    serializer_class = complaintSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('ISBN')
    serializer_class = BookSerializer

    

class FinesViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all().order_by('due_date')
    serializer_class = FineSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer



def get_event(request :  Request, event_date):
    arr = []
    if event_date is not None:
        item = Event.objects.filter(date = event_date)
        for i in item:
           
            temp={"start_time":i.start_time,
            "end_time":i.end_time,
            "title":i.title,
            "venue":i.venue,
            "description":i.description,
            "image_url":i.image_url,
            "date" : i.date}
            arr.append(temp)

        if len(arr) > 0:
            return JsonResponse({"status": "success", "data": arr}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'No Events exists'}, status=status.HTTP_404_NOT_FOUND) 

    
    return JsonResponse({'message': 'The date is not right '}, status=status.HTTP_404_NOT_FOUND) 


# class EventView(generics.CreateAPIView):

#     def create_event(self,sende)

# @api_view(['POST'])
# def create_event(request):
#     if request.method == 'POST':
#         print("here")
#         print(request.data)
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})



class GetFineAPI(generics.GenericAPIView):

    serializer_class = FineSerializer

    def get(self, request, user_id = None,*args, **kwargs):
        print("Requist from front end", request)
        if user_id is not None:
            item = Fine.objects.get(user_id = user_id)
            serializer = FineSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            
        item = Fine.objects.all().order_by('due_date')
        serializer = FineSerializer(item)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_complaint(request:Request, id):
    if request.method == 'PUT':
        item =  complaint.objects.get(id = id)
        item.status = request.data.get('status')
        item.save()
        # serializer = complaintViewSet(item)

        return JsonResponse({"status": "success"}, status=status.HTTP_200_OK)
    return JsonResponse({"status": "invalid query"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])    
def get_fine_user(request : Request, id ):
    if request.method == 'GET' :
        print("Requist from front end", request, id)
        arr=[]
        if id is not None:
            item = Fine.objects.filter(user_id = id)
            for i in item:
            
                temp={"amount_due":i.amount_due,"id":i.id,"amount_paid":i.amount_paid,"due_date":i.due_date,"book_id":i.book_id.ISBN,"user_id":i.user_id.id}
                print(i.amount_due)         
                arr.append(temp)                                  
            # print(item)
            # serializer = FineSerializer(item)
            return JsonResponse({"status": "success", "data": arr}, status=status.HTTP_200_OK)
            
        item = Fine.objects.all().order_by('due_date')
        serializer = FineSerializer(item)
        return JsonResponse({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        item =  Fine.objects.get(user_id = id, book_id =request.data.get('book_id'))
        item.amount_due = request.data.get('amount_due')
        item.amount_paid = request.data.get('amount_paid')
        item.due_date = request.data.get('due_date')
        item.save()
        serializer = FineSerializer(item)

        return JsonResponse({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



# @api_view(['PUT','PATCH'])
# def update_fine_user(request:Request):

#     print(request.data)
#         # item  = Fine.objects.get(user_id=id)
        





class IssuedViewSet(viewsets.ModelViewSet):
    queryset = Issued.objects.all().order_by('due_date')
    serializer_class = IssuedSerializer



# class EventRegister(generics.GenericAPIView):
#     """
#     API for registering events. 
#     """


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
    

    