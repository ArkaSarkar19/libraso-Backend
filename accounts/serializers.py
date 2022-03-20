from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id",'password', 'last_login', "email", "is_active",
        "staff", "admin")
        
