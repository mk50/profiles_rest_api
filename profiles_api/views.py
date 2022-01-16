from email import message

from django.shortcuts import render
from itsdangerous import serializer

from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api.models import UserProfile
from rest_framework import status

from .serializers import HelloSerializers, UserProfileSerializer
from rest_framework import viewsets
from . import permissions
from rest_framework.authentication import TokenAuthentication



class HelloView(APIView):
    serializer_class=HelloSerializers
    def get(self,request,format=None):
        alist=[
            'mohamed','mahmoud','sayed','mostafa'
        ]
        return Response(alist)

    def post(self,request):
        serializer=HelloSerializers(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            
            return Response(name)
        else:
            return Response(serializer.errors,)
# class UserProfileView(APIView):
#     def get(self,request):
#         users=UserProfile.objects.all()
#         serializer=UserProfileSerializer(users,many=True)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def post(self,request):
#         users=UserProfile.objects.all()
#         serializer=UserProfileSerializer(users,data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def get(self,request,pk):
#         users=UserProfile.objects.get(pk=pk)
#         serializer=UserProfileSerializer(users)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def put(self,request,pk):
#         users=UserProfile.objects.get(pk=pk)
#         serializer=UserProfileSerializer(users,data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         users=UserProfile.objects.get(pk=pk)
#         users.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes =[permissions.UddateOwnProfile,]
    authentication_classes=[TokenAuthentication,]
        

 

