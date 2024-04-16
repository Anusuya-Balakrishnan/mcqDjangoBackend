{
    "questions":[
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What is exception handling in Python?",
        "code": "",
        "option": [
          "A method to ignore errors in Python programs.",
          "A mechanism to handle unexpected errors that occur during program execution.",
          "A way to terminate the program when an error occurs.",
          "An alternative to using if-else statements."
        ],
        "answer": "A mechanism to handle unexpected errors that occur during program execution."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "Which keyword is used to handle exceptions in Python?",
        "code": "",
        "option": [
          "try",
          "except",
          "finally",
          "catch"
        ],
        "answer": "except"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What will happen if an exception is not handled in Python?",
        "code": "",
        "option": [
          "The program will continue executing normally.",
          "The program will terminate abruptly with an error message.",
          "The program will skip the line where the exception occurred.",
          "The program will prompt the user to handle the exception."
        ],
        "answer": "The program will terminate abruptly with an error message."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "Which of the following is NOT a built-in exception in Python?",
        "code": "",
        "option": [
          "ValueError",
          "NullPointerException",
          "TypeError",
          "SyntaxError"
        ],
        "answer": "NullPointerException"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What is the purpose of the 'finally' block in exception handling?",
        "code": "",
        "option": [
          "To catch and handle exceptions.",
          "To specify code that will be executed regardless of whether an exception occurs or not.",
          "To re-raise an exception.",
          "To ignore exceptions and continue execution."
        ],
        "answer": "To specify code that will be executed regardless of whether an exception occurs or not."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "Which keyword is used to raise an exception in Python?",
        "code": "",
        "option": [
          "raise",
          "throw",
          "exception",
          "throw_exception"
        ],
        "answer": "raise"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What will be the output of the following code?",
        "code": "\ntry:\n    num = int('abc')\nexcept ValueError:\n    print('Invalid input')",
        "option": [
          "abc",
          "Invalid input",
          "Invalid literal for int() with base 10: 'abc'",
          "None of the above"
        ],
        "answer": "Invalid input"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\ntry:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')",
        "option": [
          "10",
          "Cannot divide by zero",
          "Error",
          "None of the above"
        ],
        "answer": "Cannot divide by zero"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "When should you use the 'finally' block in exception handling?",
        "code": "",
        "option": [
          "To catch and handle exceptions.",
          "To specify code that should only execute when an exception occurs.",
          "To specify cleanup code that should always execute, regardless of whether an exception occurs or not.",
          "To specify code that should execute before the 'try' block."
        ],
        "answer": "To specify cleanup code that should always execute, regardless of whether an exception occurs or not."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "Which of the following is NOT a type of exception in Python?",
        "code": "",
        "option": [
          "RuntimeError",
          "TypeError",
          "ValueError",
          "ExceptionError"
        ],
        "answer": "ExceptionError"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What happens if an exception occurs inside a 'finally' block?",
        "code": "",
        "option": [
          "The exception is ignored and the program continues executing normally.",
          "The exception is caught and handled by the 'finally' block.",
          "The program terminates abruptly with an error message.",
          "The exception is propagated to the outer scope."
        ],
        "answer": "The exception is propagated to the outer scope."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\ntry:\n    raise Exception('An error occurred')\nexcept Exception as e:\n    print(e)",
        "option": [
          "An error occurred",
          "Exception: An error occurred",
          "Error",
          "None of the above"
        ],
        "answer": "An error occurred"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What is the purpose of the 'else' block in exception handling?",
        "code": "",
        "option": [
          "To specify code that should execute when an exception occurs.",
          "To specify cleanup code that should execute regardless of whether an exception occurs or not.",
          "To specify code that should only execute when no exception occurs.",
          "To catch and handle exceptions."
        ],
        "answer": "To specify code that should only execute when no exception occurs."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "When should you use the 'else' block in exception handling?",
        "code": "",
        "option": [
          "To catch and handle exceptions.",
          "To specify cleanup code that should always execute.",
          "To specify code that should only execute when an exception occurs.",
          "To specify code that should only execute when no exception occurs."
        ],
        "answer": "To specify code that should only execute when no exception occurs."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What happens if an exception occurs inside the 'else' block?",
        "code": "",
        "option": [
          "The exception is caught and handled by the 'else' block.",
          "The program terminates abruptly with an error message.",
          "The exception is propagated to the outer scope.",
          "The exception is ignored and the program continues executing normally."
        ],
        "answer": "The exception is ignored and the program continues executing normally."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "Which of the following statements is true about the 'try' block in exception handling?",
        "code": "",
        "option": [
          "It must always be followed by an 'except' block.",
          "It must always be followed by a 'finally' block.",
          "It can be used alone without any other blocks.",
          "It can be followed by either 'except' or 'finally' block, or both."
        ],
        "answer": "It can be followed by either 'except' or 'finally' block, or both."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "What will happen if an exception occurs inside a 'finally' block?",
        "code": "",
        "option": [
          "The exception is caught and handled by the 'finally' block.",
          "The program terminates abruptly with an error message.",
          "The exception is ignored and the program continues executing normally.",
          "The exception is propagated to the outer scope."
        ],
        "answer": "The exception is propagated to the outer scope."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 40,
      "questions": {
        "question": "Which of the following is NOT a method of the 'Exception' class in Python?",
        "code": "",
        "option": [
          "__str__",
          "__init__",
          "__name__",
          "__doc__"
        ],
        "answer": "__name__"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
  "languageId": 2,
  "topicId": 40,
  "questions": {
    "question": "Which keyword is used to handle exceptions in Python?",
    "code": "",
    "option": [
      "try",
      "except",
      "finally",
      "catch"
    ],
    "answer": "except"
  },
  "level": "beginner",
  "mark": 1,
  "time": 1
},
{
  "languageId": 2,
  "topicId": 40,
  "questions": {
    "question": "What is the output of the following code?",
    "code": "\ntry:\n    num = int('abc')\nexcept ValueError:\n    print('Invalid input')",
    "option": [
      "abc",
      "Invalid input",
      "Invalid literal for int() with base 10: 'abc'",
      "None of the above"
    ],
    "answer": "Invalid input"
  },
  "level": "beginner",
  "mark": 1,
  "time": 1
}
  ]
}