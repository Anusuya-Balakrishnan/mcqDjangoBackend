
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
import math
from django.core.exceptions import ObjectDoesNotExist

# from .emailAuthenticate import EmailBackend
from django.contrib.auth import authenticate

@api_view(["GET","POST","PATCH"])
def person(request):
    if(request.method=="GET"):
        obj=UserModel.objects.all()
        serializer=UserModelSerializer(obj,many=True)
        return Response(serializer.data)
    elif(request.method=="POST"):
        data=request.data
        serializer=UserModelSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    elif(request.method=="PUT"):
        data=request.data
        serializer=UserModelSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    elif(request.method=="PATCH"):
        data=request.data
        obj=UserModel.objects.get(name=data["name"])
        serializer=UserModelSerializer(obj,data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)


# http://127.0.0.1:8000/mcq/student/
# this api is used to create a student using post method
# using the same api ,we can get all student data by using get method
@api_view(["POST","GET"])
def student(request):
    if(request.method=="POST"):
        data=request.data
        serializer=StudentSerializer(data=data)
        print("data",serializer.is_valid())
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            user=Student.objects.get(id=request.data["id"])
            print("user",user)
            token=Token.objects.get_or_create(user=user)
            return Response({"token":token.key,"user":serializer.data})
        else:
            return Response({"Error":"invalid user"})
    elif(request.method=="GET"):
        obj=Student.objects.all()
        serializer=StudentSerializer(obj,many=True)
        return Response(serializer.data)



@api_view(['POST'])
def custom_user_check(request):
    if request.method=="POST":
        try:
            user = CustomUser.objects.get(oceanRegisterNo=request.data['oceanRegisterNo'])    
            return Response({"message":True})
        except CustomUser.DoesNotExist:
            return Response({"message":False})
    return Response({"message":"invalid"})

# this api is used to get all user details and register new user 
@api_view(['GET', 'POST'])
def custom_user_list(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            user = CustomUser.objects.get(oceanRegisterNo=request.data['oceanRegisterNo'])
            return Response({"message":False})
        except CustomUser.DoesNotExist:
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                # Extract password from the request data
                password = request.data.get('password')

                # Create and save the user
                user = serializer.save()

                # Set the password for the user
                user.set_password(password)
                user.save()
                
                # token="HEllo"
                token, created = Token.objects.get_or_create(user=user)
                return Response({"message":True,"token":token.key,"user":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def custom_user_delete(request):
    ocean_register_no = request.data.get('oceanRegisterNo')
    if ocean_register_no:
        try:
            user = CustomUser.objects.get(oceanRegisterNo=ocean_register_no)
            serializer = CustomUserSerializer(user)
            userId=serializer.data.get('id')
            resultObject=ResultModel.objects.filter(userID_id=userId)
            for eachObject in resultObject:
                eachObject.delete()
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "oceanRegisterNo not provided in the request body"}, status=status.HTTP_400_BAD_REQUEST)
        



@api_view(['POST'])
def custom_user_login(request):
    data = request.data

    if request.method == "POST":
        try:
            ocean_register_no = data['oceanRegisterNo']
            password = data['password']

            # Authenticate the user
            user = authenticate(oceanRegisterNo=ocean_register_no, password=password)

            if user is not None:
                # Authentication successful
                token, created = Token.objects.get_or_create(user=user)
                serializer = CustomUserSerializer(user)
                return Response({"message": True, "token": token.key, "studentName": serializer.data["studentName"]})
            else:
                # Authentication failed
                return Response({"message": False}, status=status.HTTP_401_UNAUTHORIZED)

        except CustomUser.DoesNotExist:
            return Response({"message": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

# # this api is used for login page of custom user
# @api_view(['POST'])
# def custom_user_login(request):
#     data=request.data
#     if request.method=="POST":
#         try:
#             # user=get_object_or_404(CustomUser,email=data['email'])
#             user=CustomUser.objects.get(oceanRegisterNo=data['oceanRegisterNo'])
#             print("user$$$$$$$$$$$$$$$$$$$$$$$",user)
#             serializer = CustomUserSerializer(user)
           
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"message":"login successfully","token":token.key,"user":serializer.data})
#         except:
#             return Response({"message":"person not exists"},status=status.HTTP_404_NOT_FOUND)
    


@api_view(["POST"])
def custom_user_logout(request):
    if(request.method=="POST"):
        request.user.auth_token.delete()
        return Response({"Message":"logout successfully"})


# this api is used to get particular user, update fields of particular user and delete user by name 
@api_view(['GET', 'PATCH', 'DELETE'])
def custom_user_detail(request, name):
    try:
        user = CustomUser.objects.get(studentName=name)
    except CustomUser.DoesNotExist:
        return Response({"message":"person not exist"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = CustomUserSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({"message":"successfully deleted"},status=status.HTTP_204_NO_CONTENT)
    

@api_view(["POST"])
def test_token(request):
    authentication_classes = [TokenAuthentication]
    if(request.method=="POST"):
        data=request.data
       # Retrieve the token from the request
        try:
            token=Token.objects.get(key=request.auth.key)
            user=token.user
            serializer = CustomUserSerializer(user)
            return Response({"message":"token value","token":token.key,"user":serializer.data})
        except:
            return Response({"message":"error"})


@api_view(['GET','POST'])
def get_mcqList(request):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        if(request.method=="GET"):
            mcqListdata = McqListDatatModel.objects.all()
            serializer = McqListDataSerializer(mcqListdata, many=True)
            return Response({"mcqList":serializer.data}) 
        elif(request.method=="POST"):
            try:
                existing_mcqName = McqListDatatModel.objects.get(mcqName=request.data.get('mcqName'))
                return Response({"message": "MCQ already created"})
            except McqListDatatModel.DoesNotExist:
                # No need to provide 'id' explicitly when creating an instance
                serializer = McqListDataSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"data": serializer.data, "Message": "mcq added successfully"})
                return Response({"Error": "invalid"})
    except CustomUser.DoesNotExist:
        return Response({"Message":"invalid"})

@api_view(['GET'])
def get_languages(request,mcqId):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        try:
            if(request.method=="GET"):
                languages = LanguageModel.objects.filter(mcqId=mcqId)
                serializer = LanguageModelSerializer(languages, many=True)
                return Response({"languages":serializer.data}) 
        except:
            return Response({"Message": "error"})
    except CustomUser.DoesNotExist:
        return Response({"Message":"invalid"})



@api_view(['POST'])
def add_languages(request):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        if(request.method=="POST"):
            try:
                existing_language = LanguageModel.objects.get(languageName=request.data.get('languageName'))
                return Response({"message": "Language already created"})
            except LanguageModel.DoesNotExist:
                serializer = LanguageModelSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"data": serializer.data, "Message": "Language added successfully"})
                return Response({"Message": "error"})
    except :
        return Response({"Message":"invalid"})

@api_view(['GET'])
def get_topic(request,languageId):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        # Filter ResultModel instances based on the user
        results = ResultModel.objects.filter(userID=user,languageId=languageId)
        completedTopic=[]
        topicList=[]
        # collecting no of topics student completed in one language
        # filtering result document based on student id and language id
        for eachResult in results:
            serializer=ResultSerializer(eachResult)
            completedTopic.append(serializer.data.get("topicId"))
        completedTopic.sort()
 
        try:
            if(request.method=="GET"):
                topic = TopicModel.objects.filter(languageId=languageId)
                serializer = TopicSerializer(topic, many=True)
                # collecting id of all topic in one language and then sorted in ascending order
                for eachData in serializer.data:
                    topicList.append(json.loads(json.dumps(eachData)).get("id"))
                topicList.sort()
                completedTopicSet=set(completedTopic)
                allTopicSet=set(topicList)
                yetToCompleteTopicList=list(allTopicSet.difference(completedTopicSet))
                toProceedTopicId=yetToCompleteTopicList[0]
                lockTopicList=yetToCompleteTopicList[1:]
                
                finalData=[]
                for eachData in serializer.data:
                    eachDocument=json.loads(json.dumps(eachData))
                    if(eachDocument.get("id") in completedTopic):
                        eachDocument["status"]="completed"
                    elif (eachDocument.get("id") in lockTopicList):
                        eachDocument['status']="lock"
                    elif (eachDocument.get("id")==toProceedTopicId):
                        eachDocument['status']="proceed"
                    finalData.append(eachDocument)
                
                return Response({"topic":finalData}) 
        except:
            return Response({"Message": "error"})
    except :
        return Response({"Message":"invalid"})


@api_view(['POST'])
def add_topic(request):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        if(request.method=="POST"):
            try:
                existing_topicName = TopicModel.objects.get(topicName=request.data.get('topicName'),languageId=request.data.get('languageId'))
                return Response({"message": "Language already created"})
            except TopicModel.DoesNotExist:
                serializer = TopicSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"data": serializer.data, "Message": "Language added successfully"})
                return Response({"Message": "error"})
    except :
        return Response({"Message":"invalid"})



@api_view(['POST'])
def add_questions(request):
    try:
        token = Token.objects.get(key=request.auth.key)
        user = token.user
        if request.method == "POST":
            serializer = QuestionSerializer(data=request.data)
            
            if serializer.is_valid():
               print("Validated Data:", serializer.validated_data)
               serializer.save()
               return Response({"data": serializer.data, "Message": "Question added successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Message": "Validation error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Token.DoesNotExist:
        return Response({"Message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"Message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def add_many_questions(request):
    try:
        # token = Token.objects.get(key=request.auth.key)
        # user = token.user
        if request.method == "POST":
            questions_data = request.data.get('questions', [])

            # Validate and save each question in the list
            responses = []
            for question_data in questions_data:
                serializer = QuestionSerializer(data=question_data)
                if serializer.is_valid():
                    serializer.save()
                    responses.append({"data": serializer.data, "Message": "Question added successfully"})
                else:
                    responses.append({"Message": "Validation error", "errors": serializer.errors})

            return Response(responses, status=status.HTTP_201_CREATED)
    except Token.DoesNotExist:
        return Response({"Message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"Message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def authorize(request):
    token = Token.objects.get(key=request.auth.key)
    user = token.user
    serializer = CustomUserSerializer(user)
    return serializer


@api_view(["GET"])
def get_questions(request, languageId, topicId):
    try:
        token = Token.objects.get(key=request.auth.key)
        user = token.user
        serializer = CustomUserSerializer(user)

        try:
            if request.method == "GET":
                questions = QuestionModel.objects.filter(languageId=languageId, topicId=topicId)
                serializer = QuestionSerializer(questions, many=True)
                questions_values = []
                regular_dict=[]
                id_list=[]
                for item in serializer.data:
                    # get all questions OrderedDict from main data and stored into list
                    regular_dict.append(json.loads(json.dumps(item["questions"])))
                    # get id of each questions
                    id_list.append(item["id"])
                try:
                    print("\nregular_dict",regular_dict)
                    for each in regular_dict:
                        # print("\neach",each)
                
                        ordered_dict = eval(each, {'OrderedDict': OrderedDict})
                        # converting OrderedDict into python dictionary 
                        myDict={}
                        for key, value in ordered_dict.items():
                            myDict[key]=value
                        questions_values.append(myDict)
                        # # Convert the OrderedDict to a regular Python dictionary
                        # question_dict = {key: value for key, value in each.items()}
                        # questions_values.append(question_dict)
                    # print("questions_values",questions_values)
                except Exception as e:
                    print("error",e)
                result={}
                for id,question in zip(id_list,questions_values):
                    result[id]=question
                resultData={"questions": serializer.data,"questions_values":result}
                return Response({"data":resultData})
        except:
            return Response({"Message": "error"})
    except:
        return Response({"Message": "invalid"})

def get_results_by_user( user_id):
    # Retrieve the user based on user_id
    user=CustomUser.objects.get(id=user_id)

    # user = get_object_or_404(CustomUser, id=user_id)

    # Filter ResultModel instances based on the user
    results = ResultModel.objects.filter(userID=user)
    
    if(len(list(results))==0):
        return list(results)
    else:
        # Extract 'answeredQuestions' values from results
        answered_questions_list = [result.answeredQuestions for result in results]
        return answered_questions_list


def addResultDatatoDatabase(result_data):
    
    serializer = ResultSerializer(data=result_data)
    if serializer.is_valid():
        serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Serializer is invalid. Errors:", serializer.errors)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_resultValue(resultData):
    totalQuestions=len(resultData)
    correctCount=0
    skippedCount=0
    wrongCount=0
    
    for eachData in resultData:
        if(resultData[eachData]["selectedAnswer"]=="time out"):
            skippedCount+=1
        elif(resultData[eachData]["isCorrect"]):
            correctCount+=1
        else:
            wrongCount+=1

        
    
    return {"correctCount":correctCount,"wrongCount":wrongCount,"skippedCount":skippedCount}

def addLeaderBoardData(leaderBoardData):
    try:
        # Try to get the existing leaderboard object
        leaderObject = LeaderBoardModel.objects.get(userID=leaderBoardData["userID"])
        print("\n leaderObject")

        # Update the fields of the existing object
        leaderObject.result =(leaderObject.result+ leaderBoardData.get("result"))//2
        leaderObject.noOfTestAttended +=1
        # Save the updated object
        leaderObject.save()
    except:
        # If the object does not exist, create a new one
        serializer = LeaderBoardSerializer(data=leaderBoardData)
        if serializer.is_valid():
            serializer.save()
            print("success")
        else:
            print(serializer.errors)
    


@api_view(["POST"])
def add_resultData(request):
    try:
        token = Token.objects.get(key=request.auth.key)
        user = token.user
        serializer = CustomUserSerializer(user)
        userData=serializer.data
        userId=int(userData["id"])
        clientData=request.data["resultData"]
        
        try:
            if request.method == "POST":
                resultQuestionList=clientData.get('resultList')
                topicId=clientData.get('topicId')
                languageId=clientData.get('languageId')
                level=clientData.get('level')
                result=0
                
                # Create ResultModel object
                current_question_id=[]
                for i in resultQuestionList:
                    current_question_id.append(int(i))                    
                    if(resultQuestionList[i]['isCorrect']):
                        result+=1
                userIdValue=CustomUser.objects.get(id=userId).id
                userName=CustomUser.objects.get(id=userId).studentName
                return_value=get_results_by_user(userId)
                result_data = {
                    'userID': userIdValue,
                    'answeredQuestions': resultQuestionList,
                    'topicId': TopicModel.objects.get(id=int(topicId)).id,
                    'languageId': LanguageModel.objects.get(id=int(languageId)).id,
                    'level': level,
                    'result':result
                    
                    }
                leaderBoardData={"username":userName,"userID":userIdValue,"result":result,"noOfTestAttended":1}
                # print("return_value",return_value)
                if( not bool(return_value)):  
                    addResultDatatoDatabase(result_data)
                    resultDict=get_resultValue(resultData=resultQuestionList)
                    
                    # adding leaderboard data
                    addLeaderBoardData(leaderBoardData)


                    resultDict["topicName"]=TopicModel.objects.get(id=int(topicId)).topicName
                    # true for new student
                    return Response({"message": True,"data":resultDict})
                else:
                    answer_value=[]
                    existing_question_id_list=[]
                    # convertin OrderedDict to list([{'1': {'selectedAnswer': '0x99fffL', 'isCorrect': True}, '2': {'selectedAnswer': 'Integer or Boolean', 'isCorrect': True}}])
                    for item in return_value:
                        answer_value.append(json.loads(json.dumps(item)))
                        
                    # existing_question_id_list ([1,2,3])
                    for eachAnswer in answer_value:
                        for key in eachAnswer:
                            existing_question_id_list.append(int(key))
                    
                    # Convert lists to sets
                    current_question_id_set = set(current_question_id)
                    existing_question_id_set = set(existing_question_id_list)

                    # Find common elements
                    common_ids = current_question_id_set.intersection(existing_question_id_set)

                    # Check if there are common elements
                    if common_ids:
                        
                        resultDict=get_resultValue(resultData=resultQuestionList)
                        resultDict["topicName"]=TopicModel.objects.get(id=int(topicId)).topicName
                            # false for person already completed this quiz
                        return Response({"message": False,"data":resultDict})
                    else:
                        print("User")
                        addResultDatatoDatabase(result_data)
                        # adding leaderboard data
                        addLeaderBoardData(leaderBoardData)
                        resultDict=get_resultValue(resultData=resultQuestionList)
                        resultDict["topicName"]=TopicModel.objects.get(id=int(topicId)).topicName
                        # true for new student
                        return Response({"message": True,"data":resultDict})
        except Exception as e:
            return Response({"Message": "error"})
    except:
        return Response({"Message": "invalid"})


def getresult(userID):
    # Retrieve the user based on user_id
    user = get_object_or_404(CustomUser, id=userID)

    # Filter ResultModel instances based on the user
    results = ResultModel.objects.filter(userID=user)
    question_id=[]
    if(len(list(results))==0):
        print("result",results)
        return False
    else:
        # Extract 'answeredQuestions' values from results
        answered_questions_list = [result.answeredQuestions for result in results]
        
        for eachData in answered_questions_list:
            question_id.append(json.loads(json.dumps(eachData)))    
    return question_id

@api_view(["POST"])
def get_resultData(request):
    try:
        token = Token.objects.get(key=request.auth.key)
        user = token.user
        serializer = CustomUserSerializer(user)
        userData=serializer.data
        userId=int(userData["id"])
        correctAnswerCount=0
        wrongAnswerCount=0
        topicName=""
        try:
            if request.method == "POST":
                questions_list=request.data.get("resultData")
                answer_list=getresult(userId)
                for eachData in answer_list:
                    for eachKey in questions_list:
                        question = QuestionModel.objects.get(id=eachKey)
                        topicName = question.topicId.topicName
                        if(eachData[eachKey]["isCorrect"]):
                            correctAnswerCount+=1
                        else:
                            wrongAnswerCount+=1
            result_data={"topicName":topicName,"correctAnswerCount":correctAnswerCount,"wrongAnswerCount":wrongAnswerCount}
            return Response({"result":result_data})
        except Exception as e:
            return Response({"result":"error"})
    except:
        return Response({"Message": "invalid"})

@api_view(["GET"])
def leaderBoardApi(request):
    try:
        # Retrieve the user associated with the token
        token = Token.objects.get(key=request.auth.key)
        user = token.user
        # Serialize the user data
        serializer = CustomUserSerializer(user)
        leaderBoardObjects=LeaderBoardModel.objects.all()
        leaderBoardSerializer=LeaderBoardSerializer(leaderBoardObjects,many=True)
        data=leaderBoardSerializer.data
        print(data)
        return Response({"data":data})
    except Token.DoesNotExist:
        return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
    
    except ObjectDoesNotExist:
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"error": f"An error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(["GET"])
# def leaderBoardApi(request):
#     try:
#         # Retrieve the user associated with the token
#         token = Token.objects.get(key=request.auth.key)
#         user = token.user
#         # Serialize the user data
#         serializer = CustomUserSerializer(user)
#         userData = serializer.data
#         currentUserName = userData.get("studentName")

#         # Retrieve all ResultModel objects
#         all_results = ResultModel.objects.all()

#         # Serialize the queryset
#         serializer = ResultSerializer(all_results, many=True)
#         result_data = serializer.data
        
#         # Prepare the leaderboard data
#         leaderboard_data = {}
#         user_results = {}

#         for result in result_data:
#             user_id = result.get("userID")
#             user_name = CustomUser.objects.get(id=user_id).studentName

#             if user_name not in user_results:
#                 user_results[user_name] = {"result": 0, "noOfTestAttended": 0}
            
#             user_results[user_name]["userID"]=user_id
#             user_results[user_name]["result"] += result.get("result")
#             user_results[user_name]["noOfTestAttended"] += 1

#         # Calculate average result
#         for user_name, data in user_results.items():
#             data["result"] //= data["noOfTestAttended"]

#         # Sort leaderboard data based on result in descending order
#         sorted_leaderboard = sorted(user_results.items(), key=lambda x: x[1]["result"], reverse=True)
        
#         # Prepare final leaderboard datag
#         # leaderboard_data = [{"username": name, **data, "currentUser": name == currentUserName} for name, data in sorted_leaderboard]
#         leaderboard_data = [{"username": name, **data} for name, data in sorted_leaderboard]
#         # for eachData in leaderboard_data:
#         #     print(eachData)
#         #     serializer = LeaderBoardSerializer(data=eachData)
#         #     if serializer.is_valid():
#         #         print("saved")
#         #         serializer.save()
#         #     else:
#         #         print(serializer.errors)

#         return Response({"message": leaderboard_data})

#     except Token.DoesNotExist:
#         return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
    
#     except ObjectDoesNotExist:
#         return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     except Exception as e:
#         return Response({"error": f"An error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(["GET"])
# def leaderBoardApi(request):
#     try:
#         token = Token.objects.get(key=request.auth.key)
#         user = token.user
#         serializer = CustomUserSerializer(user)
#         userData=serializer.data
#         currentUserName=userData.get("studentName")
#         # print("currentUserName",currentUserName)
#         if(request.method=="GET"):
#             try:
#                 # Retrieve all ResultModel objects
#                 all_results = ResultModel.objects.all()

#                 # Serialize the queryset if needed
#                 serializer = ResultSerializer(all_results, many=True)
#                 result_data = json.loads(json.dumps(serializer.data))
#                 resultList=[]
#                 for eachResult in result_data:
#                     resultDict={}
#                     currentUser=False
#                     for eachKey in eachResult:
#                         if eachKey=="userID":
#                             # Retrieve CustomUser object by ID
#                             custom_user = CustomUser.objects.get(id=eachResult["userID"])
#                             # Serialize the CustomUser object to get the studentName
#                             custom_serializer = CustomUserSerializer(custom_user)
#                             user_data = custom_serializer.data
#                             user_name = user_data.get("studentName")
#                             if(user_name==currentUserName):
#                                 currentUser=True
#                             resultDict["username"]=user_name
                            
#                         elif eachKey=="result":
#                             resultDict["result"]=eachResult[eachKey]
#                         resultDict["currentUser"]=currentUser
#                     resultList.append(resultDict)
#                 usernameList=[]
#                 data={}
#                 userResultData=[]
#                 for eachData in resultList:
#                     if eachData["username"] in usernameList:
#                         for userResult in userResultData:
#                             if userResult["username"]==eachData["username"]:
#                                 userResult["result"]= (userResult["result"]+eachData["result"])//2
#                                 userResult["noOfTestAttended"]+=1
#                     else:
#                         data={
#                             "username": eachData["username"],
#                             "result": eachData["result"],
#                             "currentUser":eachData["currentUser"],
#                             "noOfTestAttended":1
#                             }
#                         usernameList.append(eachData["username"])
#                         userResultData.append(data)
#                 # Sort userResultData based on the "result" value in descending order
#                 userResultData = sorted(userResultData, key=lambda x: x["result"], reverse=True)
#                 print("userResultData",userResultData)
#                 return Response({"message":userResultData})
#             except Exception as e:
#                 return Response({"error":f"error message{e}"})
#         return Response({"message":"invalid Request"})
#     except:
#         return Response({"Message":"invalid"})

def getAnswer(resultData):
    questionNos=list(resultData.keys())
    answerList=[]
    finalList=[]
    questionId=[]
    questionsList=[]
    for eachQuestion in questionNos:
        questionObject=QuestionModel.objects.get(id=eachQuestion)
        serializer=QuestionSerializer(questionObject)
        questionId.append(serializer.data["id"])
        answerList.append(json.loads(json.dumps(serializer.data["questions"])))
            
    for eachAnswer in answerList:
        ordered_dict = eval(eachAnswer, {'OrderedDict': OrderedDict})
        myDict={}
        for key, value in ordered_dict.items():
            myDict[key]=value
        questionsList.append(myDict)
    for key,value in zip(questionId,questionsList):
        answerDict=dict(value)
        answerDict["selectedAnswer"]=resultData[str(key)].get("selectedAnswer")
        answerDict["isCorrect"]=resultData[str(key)].get("isCorrect")
        answerDict["id"]=key
        finalList.append(answerDict)
    return finalList



@api_view(["POST"])
def showResult(request):
    try:
        serializer=authorize(request)
        if(request.method=="POST"):
            resultData=request.data["answeredQuestions"]
            finalList=getAnswer(resultData)

            return Response({"data":finalList})

    except Exception as e:
        return Response({"error":f"error message{e}"})



@api_view(["GET"])
def getDashboard(request):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        
        if(request.method=="GET"):
            results = ResultModel.objects.filter(userID=user)
            completedTopic=[]
        # collecting no of topics student completed in one language
        # filtering result document based on student id and language id
            topic = TopicModel.objects.filter()
            serializer = TopicSerializer(topic, many=True)
            totalTopic=len(serializer.data)
            for eachResult in results:
                serializer=ResultSerializer(eachResult)
                completedTopic.append(serializer.data.get("topicId"))
            

            noOfTopicCompleted=len(completedTopic)
            noOfPendingTopic=totalTopic-noOfTopicCompleted
            completedPercentage=math.floor((noOfTopicCompleted/totalTopic)*100)
            # pendingPercentage=math.floor(((totalTopic-noOfTopicCompleted)/totalTopic)*100)
            

            # collecting no of Language
            language=LanguageModel.objects.filter()
            resultData=[]
            for eachLanguage in language:
                eachSerializerObject=LanguageModelSerializer(eachLanguage)
                languageId=eachSerializerObject.data.get("id")
                topic = TopicModel.objects.filter(languageId=languageId)
                serializer = TopicSerializer(topic, many=True)
                totalTopic=len(serializer.data)
                resultObjects=ResultModel.objects.filter(userID=user,languageId=languageId)
                serializer=ResultSerializer(resultObjects,many=True)
                resultTopicCompleted=len(serializer.data)
                if(totalTopic>0 and resultTopicCompleted>0):
                    completedPercent=math.floor((resultTopicCompleted/totalTopic)*100)
                    resultData.append({"languageName":eachSerializerObject.data.get("languageName"),
                                       "languageId":languageId
                                       ,"totalTopic":totalTopic,"completedTopic":resultTopicCompleted,"completedPercentage":completedPercent})
            return Response({"noOfTopicCompleted":noOfTopicCompleted,"noOfPendingTopic":noOfPendingTopic,
                             "completedPercentage":completedPercentage,"resultData":resultData})
    except Exception as e:
        return Response({"error":f"error message{e}"})



@api_view(["GET"])
def getTopicCompleted(request,languageId):
    try:
        # converting token into user object else it return error
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)

        if(request.method=="GET"):
            # collecting topic object based on language id
            topic = TopicModel.objects.filter(languageId=languageId)

            # get language name by using language id
            langObject=LanguageModel.objects.get(id=languageId)
            languageName=LanguageModelSerializer(langObject).data.get("languageName")

            # converting topic object into json format using serializer
            topicSerializer = TopicSerializer(topic, many=True)
            
            # total no of topics
            totalTopic=len(topicSerializer.data)

            # filtering result collection based on user id and language id
            results = ResultModel.objects.filter(userID=user,languageId=languageId)
            resultSerializer=ResultSerializer(results,many=True)
            
            # total no of completed topic
            completedTopicCount=len(resultSerializer.data)


            topicIdList=[]
            for eachResult in results:
                # get result object id
                resultId=ResultSerializer(eachResult).data.get("id")
                
                # get topic object from result object
                topicId=ResultSerializer(eachResult).data.get("topicId")
                # get topic object
                topic = TopicModel.objects.get(id=topicId)
                topicObject=TopicSerializer(topic)
                # get topic name using topicId 
                topicName=topicObject.data.get("topicName")
    
                topicIdList.append({"topicName":topicName,"resultId":resultId})

            # final result value
            resultData={"Totaltopic":totalTopic,
                        "completedTopicCount":completedTopicCount,"topicIdList":topicIdList,
                        "languageName":languageName}
            return Response(resultData)

    except Exception as e:
        return Response({"error":f"error message{e}"})




@api_view(["GET"])
def answerValueInTopicPage(request,resultId):
    try:
        authorize(request)
        if request.method=="GET":
            resultObject=ResultModel.objects.get(id=resultId)
            resultSerializer=ResultSerializer(resultObject).data
            result={}
            for each in resultSerializer:
                if(each=="answeredQuestions"):
                    dictValue = eval(resultSerializer[each])
                    result = {key: dict(value) for key, value in dictValue.items()}
            data=getAnswer(result)
            return Response(data)
    except Exception as e:
        return Response({"error":f"error message{e}"})