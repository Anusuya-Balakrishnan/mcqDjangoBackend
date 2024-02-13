

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
   "questions":[
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "What is the correct syntax to declare a variable in Java?",
            "option": [
                "variable int x;",
                "int x = 10;",
                "int x;",
                "declare x = 10;"
            ],
            "answer": "int x = 10;"
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
            "option": [
                "123variable",
                "_myVariable",
                "my Variable",
                "variable@123"
            ],
            "answer": "_myVariable"
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
            "option": [
                "0",
                "null",
                "undefined",
                "1"
            ],
            "answer": "0"
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
            "option": [
                "int",
                "float",
                "double",
                "decimal"
            ],
            "answer": "double"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "How can you make a constant variable in Java?",
            "option": [
                "final int x = 10;",
                "const x = 10;",
                "int constant x = 10;",
                "static int x = 10;"
            ],
            "answer": "final int x = 10;"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "What is the scope of a local variable in Java?",
            "option": [
                "Global",
                "Class",
                "Method",
                "Package"
            ],
            "answer": "Method"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "Which keyword is used to declare a constant in Java?",
            "option": [
                "static",
                "const",
                "final",
                "readonly"
            ],
            "answer": "final"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "What is the purpose of the 'this' keyword in Java?",
            "option": [
                "Refers to the current instance of the class",
                "Refers to the superclass",
                "Refers to a static variable",
                "Refers to a local variable"
            ],
            "answer": "Refers to the current instance of the class"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "What is the range of a byte variable in Java?",
            "option": [
                "-128 to 127",
                "0 to 255",
                "0 to 65535",
                "No limit"
            ],
            "answer": "-128 to 127"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "How do you declare a long variable in Java?",
            "option": [
                "long x = 100L;",
                "int x = 100;",
                "float x = 100.0;",
                "double x = 100.0;"
            ],
            "answer": "long x = 100L;"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "Which of the following is a valid way to concatenate strings in Java?",
            "option": [
                "str1 + str2",
                "str1 .concat(str2)",
                "str1.join(str2)",
                "All of the above"
            ],
            "answer": "All of the above"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "What is the default value of a boolean variable in Java?",
            "option": [
                "true",
                "false",
                "0",
                "null"
            ],
            "answer": "false"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "How do you declare a constant array in Java?",
            "option": [
                "final int[] numbers = {1, 2, 3};",
                "const int[] numbers = {1, 2, 3};",
                "static final int[] numbers = {1, 2, 3};",
                "int[const] numbers = {1, 2, 3};"
            ],
            "answer": "final int[] numbers = {1, 2, 3};"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "What is the default value of an object variable in Java?",
            "option": [
                "0",
                "null",
                "undefined",
                "1"
            ],
            "answer": "null"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "Which data type is used to represent characters in Java?",
            "option": [
                "char",
                "string",
                "character",
                "chr"
            ],
            "answer": "char"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "How do you declare a constant String in Java?",
            "option": [
                "const String name = 'John';",
                "final String name = 'John';",
                "static final String name = 'John';",
                "String const name = 'John';"
            ],
            "answer": "final String name = 'John';"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "What will be the result of the expression: 10 + 5 / 2?",
            "option": [
                "12.5",
                "15",
                "11",
                "Error"
            ],
            "answer": "12"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "Which of the following is a valid declaration of a double variable?",
            "option": [
                "double x = 10;",
                "float x = 10.0;",
                "double x = 10.0;",
                "int x = 10.0;"
            ],
            "answer": "double x = 10.0;"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 1,
        "topicId": 1,
        "questions": {
            "question": "What is the purpose of the 'static' keyword in Java?",
            "option": [
                "To make a variable non-modifiable",
                "To make a variable belong to the class rather than an instance",
                "To declare a constant",
                "To define a method as abstract"
            ],
            "answer": "To make a variable belong to the class rather than an instance"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    }
]

}



{
  "questions": 
  [
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