# serializers.py
from rest_framework import serializers

from .models import   Book, Fine



class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("ISBN", "title", "author", "description", "edition","rating","books_available","book_Image_url" )

class FineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fine
        fields = ("user_id", "amount","due_date")
