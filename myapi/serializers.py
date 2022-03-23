# serializers.py
from rest_framework import serializers

from .models import   Book, Fine,Issued



class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("ISBN", "title", "author", "description", "edition","rating","books_available","book_Image_url" )

class FineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fine
<<<<<<< HEAD
        fields = ("user_id", "amount_paid","due_date","book_id","amount_due")

class IssuedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issued
        fields = ("user_id", "issued_date","due_date","book_id")
=======
        fields = ("user_id", "amount","due_date", "book_id")
>>>>>>> a70e9ba01b652b0c6e68371bd3d1e0ba7640d61b
