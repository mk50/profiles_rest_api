from os import name
from pyexpat import model
from django.forms import fields
from rest_framework import serializers
from .models import *
class HelloSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=30)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['id','email','name','password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password=validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileFeedItem
        fields=['id','user_profile','status_txt','created_on']
        extra_kwargs={'user_profile':{'read_only':True}}
        