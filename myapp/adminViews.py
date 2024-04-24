
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
    

@api_view(["DELETE","PATCH"])
def quizName_update_delete(request):
    if request.method == "PATCH":  # Update functionality
        try:
            mcq_instance = McqListDatatModel.objects.get(id=request.data.get('mcqId'))
            serializer = McqListDataSerializer(mcq_instance,data={'mcqName': request.data.get('newMcqName')}, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response({"data": "mcq updated successfully"}, status=status.HTTP_200_OK)
        except McqListDatatModel.DoesNotExist:
            return Response({"data": "MCQ not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":  # Delete functionality
        try:
            print("HEllo Delete\n")
            mcq_instance = McqListDatatModel.objects.get(id=request.data.get('mcqId'))
            mcq_instance.delete()
            return Response({"data": "success"}, status=status.HTTP_204_NO_CONTENT)
        except McqListDatatModel.DoesNotExist:
            return Response({"data": "failure"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST','PATCH','DELETE'])
def languages_list_update(request,mcqId):
    try:
        if(request.method=="GET"):
            languages = LanguageModel.objects.filter(mcqId=mcqId)
            serializer = LanguageModelSerializer(languages, many=True)
            return Response({"languages":serializer.data}) 
        elif request.method == "POST":
            try:
                existing_language = LanguageModel.objects.get(languageName=request.data.get('languageName'))
                return Response({"message": "Language already created"})
            except LanguageModel.DoesNotExist:
                serializer = LanguageModelSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"data": serializer.data, "message": "Language added successfully"})
                return Response({"message": "error"})
        elif request.method == "PATCH":
            try:
                language = LanguageModel.objects.get(id=request.data.get("id"), mcqId=mcqId)
            except LanguageModel.DoesNotExist:
                return Response({"message": "Language not found"}, status=404)
            
            serializer = LanguageModelSerializer(language, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Language updated successfully"})
            
            return Response(serializer.errors, status=400)
        
        elif request.method == "DELETE":
            try:
                language = LanguageModel.objects.get(id=request.data.get("id"), mcqId=mcqId)
            except LanguageModel.DoesNotExist:
                return Response({"message": "Language not found"}, status=404)
            
            language.delete()
            return Response({"message": "Language deleted successfully"})
    except Exception as e:
        return Response({"Message": f"error ${e}"})
    

@api_view(['GET','POST','PATCH','DELETE'])
def topic_list_update(request,languageId):
    try:
        if request.method=="GET":
            topic = TopicModel.objects.filter(languageId=languageId)
            serializer = TopicSerializer(topic, many=True)
            return Response({"data":serializer.data})
            # # collecting id of all topic in one language and then sorted in ascending order
            # for eachData in serializer.data:
            #     topicList.append(json.loads(json.dumps(eachData)).get("id"))
        elif request.method=="POST":
            try:
                existing_topicName = TopicModel.objects.get(topicName=request.data.get('topicName'),languageId=request.data.get('languageId'))
                return Response({"message": "topic already created"})
            except TopicModel.DoesNotExist:
                serializer = TopicSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({ "message": "topic added successfully"})
                return Response({"Message": "error"})
        elif request.method == "DELETE":
            try:
                topic = TopicModel.objects.get(id=request.data.get("id"), languageId=languageId)
            except TopicModel.DoesNotExist:
                return Response({"message": "topic not found"}, status=404)
            
            topic.delete()
            return Response({"message": "topic deleted successfully"})
    except Exception as e:
        return Response({"Message": f"error ${e}"})
