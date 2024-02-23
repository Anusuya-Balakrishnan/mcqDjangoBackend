
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
# from rest_framework.permissions import AllowAny
# from knox.models import AuthToken
from rest_framework import status
# from rest_framework import generics
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
import ast
from collections import OrderedDict
# from .emailAuthenticate import EmailBackend
from django.contrib.auth import authenticate


@api_view(["GET","POST"])
def quiz_List(request):
    if(request.method=="GET"):
        try:
            mcqListdata = McqListDatatModel.objects.all()
            serializer = McqListDataSerializer(mcqListdata, many=True)
            return Response({"data":serializer.data})
        except:
            return Response({"data":None},status=status.HTTP_400_BAD_REQUEST)
    elif (request.method=="POST"):
        try:
            existing_mcqName = McqListDatatModel.objects.get(mcqName=request.data.get('mcqName'))
            return Response({"data": "MCQ already created"},status=status.HTTP_400_BAD_REQUEST)
        except McqListDatatModel.DoesNotExist:
            serializer = McqListDataSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"data": "mcq added successfully"},status=status.HTTP_201_CREATED)
            return Response({"Error": "invalid"})
        