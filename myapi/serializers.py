# serializers.py
from email.policy import default
from rest_framework import serializers

from .models import   Book, Fine,Issued



class BookSerializer(serializers.HyperlinkedModelSerializer):

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

class FineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fine
        fields = '__all__'


class IssuedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issued
        fields = '__all__'
