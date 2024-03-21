

from django.urls import path
# from .views import UserDetailView,UserListView,CreateUserView
from . import views
from . import adminViews

urlpatterns = [

# client side url
    path("user/",views.person,name="person"),
    path("student/",views.student,name="student"),
    path('users/', views.custom_user_list, name='custom_user_list'),
    path("custom_user_delete/",views.custom_user_delete,name='delete_custom_user'),
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
    path("showResult/",views.showResult,name="showResult"),
    path("dashboard/",views.getDashboard,name="getDashboard"),
    path("resultTopicList/<int:languageId>/",views.getTopicCompleted,name="resultTopicList"),
# admin side url
    path("quiz_list/",adminViews.quiz_List,name="add_update_quiz"),
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

{"languageId":1,
"topicId":1,
"questions":{"question":"Who invented Java Programming?","code":"","option":["Guido van Rossum","James Gosling","Dennis Ritchie","Bjarne Stroustrup"],"answer":"James Gosling"},
"level":"beginner",
"mark":1,
"time":1
}


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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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
            "code":"",
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

# java beginner I

{"questions":[

{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the output of the following code snippet?",
"code":"String str = \"Hello\";\nSystem.out.println(str.substring(2, 4));",
"option":["a) Hel","b) lo","c) ell","d) llo"],
"answer":"c) ell"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"Which of the following is not a valid access specifier in Java?",
"code":"",
"option":["a) public","b) protected","c) private","d) package"],
"answer":"d) package"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What does the \"break\" statement do in Java?",
"code":"",
"option":["a) Exits the loop or switch statement","b) Continues to the next iteration of the loop","c) Skips the current iteration of the loop","d) None of the above"],
"answer":"a) Exits the loop or switch statement"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"Which of the following is not a valid loop in Java?",
"code":"",
"option":["a) for","b) foreach","c) while","d) do-while"],
"answer":"b) foreach"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the output of the following code snippet?",
"code":"int i = 10;\nSystem.out.println(i++);",
"option":["a) 10","b) 11","c) 12","d) Compile error"],
"answer":"a) 10"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the output of the following code snippet?",
"code":"System.out.println(Math.min(Double.MIN_VALUE, 0.0));",
"option":["a) Double.MIN_VALUE","b) 0.0","c) 0.0 (negative)","d) 0.0 (positive)"],
"answer":"b) 0.0"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the output of the following code snippet?",
"code":"System.out.println(10 + 20 + \"Hello\");",
"option":["a) 30Hello","b) 1020Hello","c) Compile error","d) Runtime error"],
"answer":"a) 30Hello"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"Which of the following is not a Java keyword?",
"code":"",
"option":["a) sizeof","b) instanceof","c) native","d) transient"],
"answer":"a) sizeof"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the output of the following code snippet?",
"code":"System.out.println(\"5\" + 3 + 2);",
"option":["a) 532","b) 10","c) 5+3+2","d) Compile error"],
"answer":"a) 532"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"Which of the following is used to create an object in Java?",
"code":"",
"option":["a) new","b) class","c) create","d) instanceOf"],
"answer":"a) new"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the output of the following code snippet?",
"code":"System.out.println(5 == 5.0);",
"option":["a) true","b) false","c) Compile error","d) Runtime error"],
"answer":"a) true"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the output of the following code snippet?",
"code":"System.out.println(10 % 3);",
"option":["a) 1","b) 2","c) 3","d) 0"],
"answer":"a) 1"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"Which of the following statements is true about interfaces in Java?",
"code":"",
"option":["a) Interfaces can have constructors.","b) Interfaces can have method definitions.","c) Interfaces can extend classes.","d) Interfaces can have instance variables."],
"answer":"b) Interfaces can have method definitions."
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the output of the following code snippet?",
"code":"System.out.println(\"abc\".toUpperCase());",
"option":["a) abc","b) ABC","c) Compile error","d) Runtime error"],
"answer":"b) ABC"
},
"level":"beginner",
"mark":1,
"time":1
}
,
{
"languageId":1,
"topicId":1,
"questions":{
"question":"What is the correct way to declare a string variable in Java?",
"code":"",
"option":["a) string s;","b) String s;","c) string s = "";","d) String s = "";"],
"answer":"d) String s = "";"
},
"level":"beginner",
"mark":1,
"time":1
}]}



