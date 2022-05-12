# serializers.py
from dataclasses import fields
from email.policy import default
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from .models import   Book, Fine,Issued,complaint, Event
from accounts.serializers import OurUsersSerializer, OurUsersDetailSerializer
from accounts.models import OurUser

# class MyRelatedField(serializers.RelatedField):
#     def to_representation(self, obj):
#         return {
#             'id': obj.pk,
#         }
class complaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = complaint
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):

    title=serializers.CharField(max_length=60)
    author=serializers.CharField(max_length=60)
    edition=serializers.IntegerField(default=0)
    description=serializers.CharField(max_length=256)
    ISBN=serializers.CharField(max_length=13)
    subjects=serializers.CharField(max_length=60)

    rating=serializers.FloatField(default=0)
    books_available=serializers.CharField(max_length=60)
    book_Image_url=serializers.URLField(default="")

    class Meta:
        model = Book
        fields = "__all__"

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN']
 


class FineSerializer(serializers.ModelSerializer):

    # user_id = PresentablePrimaryKeyRelatedField(
    #     queryset = OurUser.objects.all(),
    #     presentation_serializer = OurUsersDetailSerializer)
    # amount_due = serializers.FloatField()
    # amount_paid=serializers.FloatField()
    # due_date = serializers.DateTimeField()
    # book_id = PresentablePrimaryKeyRelatedField(
    #     queryset = Book.objects.all(),
    #     presentation_serializer = BookDetailSerializer)

    class Meta:
        model = Fine
        fields = '__all__'


class IssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issued
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
