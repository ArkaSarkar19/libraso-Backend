from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .models import OurUser

class OurUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurUser
        fields = "__all__"        


#Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'gender',  'user_type', 'password')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        # if 'email' not in validated_data.keys():
        #     validated_data['email'] = validated_dataNone
        
        
        # user=OurUsers.objects.create_user (
        #     validated_data['username'], validated_data['user_type'], validated_data['email'], validated_data['password'], 
        #     validated_data['first_name'],
        #     validated_data['last_name'], validated_data['gender'], validated_data['partner_id'], validated_data['sheroes_id']
        # )
        user=OurUser.objects.create_user(**validated_data)
        return user

#Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        ##uncomment this if you add isdeleted field in OurUsers model
        # if user and !user.is_deleted:
        #     return user
        # raise serializers.ValidationError("Incorrect Credentials")

        #comment this when you uncomment above
        if user:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
