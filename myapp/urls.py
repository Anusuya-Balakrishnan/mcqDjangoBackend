

from django.urls import path
# from .views import UserDetailView,UserListView,CreateUserView
from . import views

urlpatterns = [

    path("user/",views.person,name="person"),
    path("student/",views.student,name="student"),
    path('users/', views.custom_user_list, name='custom_user_list'),
    path("custom_user_check/",views.custom_user_check,name="custom_user_check"),
    path("userLogin/",views.custom_user_login,name='custom_login'),
    path("userLogout/",views.custom_user_logout,name="custom_logout"),
    path("test_token/",views.test_token,name="test_token"),
    path("get_mcqList/",views.get_mcqList,name="get_mcqList"),
    path('add_languages/',views.add_languages,name='add_languages'),
    path('get_language/<int:mcqId>/',views.get_languages,name='get_languages'),
    path('add_topic/',views.add_topic,name='add_topic'),
    path('get_topic/<int:languageId>/',views.get_topic,name='get_topic'),
    path('add_questions/',views.add_questions,name="add_questions"),
    path('add_many_questions/',views.add_many_questions,name="add_many_questions"),
    path('get_questions/<int:languageId>/<int:topicId>/',views.get_questions,name='get_questions'),
    path("add_resultData/",views.add_resultData,name="add_resultData"),
    path("get_resultData/",views.get_resultData,name="get_resultData"),
    path("leaderBoardApi/",views.leaderBoardApi,name="leaderBoardApi"),
    path('users/<str:name>/', views.custom_user_detail, name='custom_user_detail'),
]

# {
# "studentName":"siva",
# "date":"2022-01-18T12:30:45.123Z",
# "dob":"1990-05-15T08:00:00+02:00",
# "mobileNumber":"9489645465",
# "address":"pondy",
# "qualification":"B.Tech",
# "nationality":"Indian",
# "workingDesignation":"developer",
# "studentCollegeName":"christ",
# "email":"siva@gmail.com",
# "whatsappNumber":"9489645465",
# "gender":"male"
# }

# {"languageId":1,
# "topicId":1,
# "questions":{"question":"Who invented Java Programming?","option":["Guido van Rossum","James Gosling","Dennis Ritchie","Bjarne Stroustrup"],"answer":"James Gosling"},
# "level":"beginner",
# "mark":1,
# "time":1
# }


# http://127.0.0.1:8000/mcq/get_mcqList/

{
    "mcqName":"programming"
}
# http://127.0.0.1:8000/mcq/add_languages/
{
    "mcqId":1,
    "languageName":"Java"
}

# add_topic
{
    "languageId":1,
    "topicName":"Variables"
}
# add_many_questions
{
  "questions": [
    {
      "languageId": 1,
      "topicId": 1,
      "questions": {
        "question": "What is a variable in Java?",
        "option": ["A reserved keyword", "A storage location with a specific type and identifier", "A method in a class", "A loop construct"],
        "answer": "A storage location with a specific type and identifier"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 1,
      "topicId": 1,
      "questions": {
        "question": "Which of the following is a valid variable name in Java?",
        "option": ["123variable", "variable@name", "_variableName", "class"],
        "answer": "_variableName"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
     {
      "languageId": 1,
      "topicId": 1,
      "questions": {
        "question": "What is the default value of an int variable in Java?",
        "option": ["0", "0.0", "null", "false"],
        "answer": "0"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    }
     ,{
      "languageId": 1,
      "topicId": 1,
      "questions": {
        "question": "How do you declare a constant in Java?",
        "option": ["Using the 'final' keyword", "Using the 'const' keyword", "Using the 'static' keyword", "Constants are not allowed in Java"],
        "answer": "Using the 'final' keyword"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 1,
      "topicId": 1,
      "questions": {
        "question": "Which data type is used to store decimal numbers in Java?",
        "option": ["int", "double", "char","boolean"],
        "answer": "double"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    }
    
  ]
}