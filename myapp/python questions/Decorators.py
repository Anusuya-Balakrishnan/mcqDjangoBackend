{
    "questions":[
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "What is a decorator in Python?",
        "code": "",
        "option": [
          "A decorator is a function that modifies the behavior of another function.",
          "A decorator is a data structure used to store key-value pairs.",
          "A decorator is a Python module for graphical user interface design.",
          "A decorator is a built-in Python keyword used for exception handling."
        ],
        "answer": "A decorator is a function that modifies the behavior of another function."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "Which symbol is used to apply a decorator in Python?",
        "code": "",
        "option": [
          "@",
          "&",
          "$",
          "#"
        ],
        "answer": "@"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "What is the purpose of using decorators in Python?",
        "code": "",
        "option": [
          "To add new functionality to existing functions without modifying their structure.",
          "To remove functionality from existing functions.",
          "To rename existing functions.",
          "To create new functions."
        ],
        "answer": "To add new functionality to existing functions without modifying their structure."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "Which of the following statements about decorators in Python is true?",
        "code": "",
        "option": [
          "Decorators can only be applied to class methods.",
          "Decorators can only be applied to built-in functions.",
          "Decorators can be nested.",
          "Decorators cannot accept arguments."
        ],
        "answer": "Decorators can be nested."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "Which built-in Python function can be used to define a decorator?",
        "code": "",
        "option": [
          "def",
          "lambda",
          "decorator",
          "classmethod"
        ],
        "answer": "def"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "What is the output of the following code snippet?",
        "code": "def my_decorator(func):\n    def wrapper():\n        print('Something is happening before the function is called.')\n        func()\n        print('Something is happening after the function is called.')\n    return wrapper\n\n@my_decorator\ndef say_hello():\n    print('Hello!')\n\nsay_hello()",
        "option": [
          "Hello!",
          "Something is happening before the function is called. Hello! Something is happening after the function is called.",
          "Something is happening before the function is called. Something is happening after the function is called. Hello!",
          "Something is happening before the function is called. Hello!"
        ],
        "answer": "Something is happening before the function is called. Hello! Something is happening after the function is called."
      },
      "level": "intermediate",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "Which of the following is NOT a correct way to apply a decorator in Python?",
        "code": "",
        "option": [
          "Using the @ symbol followed by the decorator name above the function to be decorated.",
          "Passing the function to be decorated as an argument to the decorator function.",
          "Using the decorator function as a parameter to the function to be decorated.",
          "All of the above are correct ways to apply a decorator."
        ],
        "answer": "All of the above are correct ways to apply a decorator."
      },
      "level": "intermediate",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "Which of the following decorators can be used to measure the execution time of a function?",
        "code": "",
        "option": [
          "@staticmethod",
          "@classmethod",
          "@property",
          "@timeit"
        ],
        "answer": "@timeit"
      },
      "level": "intermediate",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "What is the purpose of a nested decorator in Python?",
        "code": "",
        "option": [
          "To apply multiple decorators to a single function.",
          "To apply decorators to nested functions.",
          "To apply decorators to class methods.",
          "To create decorators inside a class."
        ],
        "answer": "To apply multiple decorators to a single function."
      },
      "level": "intermediate",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "Which of the following statements about class decorators in Python is true?",
        "code": "",
        "option": [
          "Class decorators can only be applied to class methods.",
          "Class decorators can only be applied to built-in functions.",
          "Class decorators can only accept one argument.",
          "Class decorators can accept any number of arguments."
        ],
        "answer": "Class decorators can accept any number of arguments."
      },
      "level": "intermediate",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "What is the output of the following code snippet?",
        "code": "def repeat(num):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            for _ in range(num):\n                func(*args, **kwargs)\n        return wrapper\n    return decorator\n\n@repeat(3)\ndef greet(name):\n    print('Hello, ' + name)\n\ngreet('Alice')",
        "option": [
          "Hello, Alice",
          "Hello, AliceHello, AliceHello, Alice",
          "Hello, AliceAliceAlice",
          "None of the above"
        ],
        "answer": "Hello, AliceHello, AliceHello, Alice"
      },
      "level": "advanced",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "Which of the following is NOT a valid use case for decorators in Python?",
        "code": "",
        "option": [
          "Logging",
          "Caching",
          "Asynchronous programming",
          "Dynamic typing"
        ],
        "answer": "Dynamic typing"
      },
      "level": "advanced",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "What is a parameterized decorator in Python?",
        "code": "",
        "option": [
          "A decorator that takes parameters.",
          "A decorator applied to function parameters.",
          "A decorator defined within a function.",
          "A decorator applied to class parameters."
        ],
        "answer": "A decorator that takes parameters."
      },
      "level": "advanced",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 46,
      "questions": {
        "question": "What is the purpose of using the functools module in Python decorators?",
        "code": "",
        "option": [
          "To define decorators with additional functionality.",
          "To create decorators for class methods.",
          "To create decorators that accept parameters.",
          "To simplify the implementation of decorators."
        ],
        "answer": "To simplify the implementation of decorators."
      },
      "level": "advanced",
      "mark": 1,
      "time": 1
    },
    {
        "languageId": 2,
        "topicId": 46,
        "questions": {
          "question": "What is the syntax for applying a decorator to a function in Python?",
          "code": "",
          "option": [
            "decorator_name",
            "@decorator_name",
            "#decorator_name",
            "&decorator_name"
          ],
          "answer": "@decorator_name"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
      },
      {
        "languageId": 2,
        "topicId": 46,
        "questions": {
          "question": "Can decorators be applied to class methods in Python?",
          "code": "",
          "option": [
            "Yes, but only using class decorators.",
            "Yes, using both function and class decorators.",
            "No, decorators cannot be applied to class methods.",
            "None of the above."
          ],
          "answer": "Yes, using both function and class decorators."
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
      },
      {
        "languageId": 2,
        "topicId": 46,
        "questions": {
          "question": "What is the purpose of the functools.wraps decorator in Python?",
          "code": "",
          "option": [
            "To create nested decorators.",
            "To remove decorators from functions.",
            "To preserve the metadata of the original function when using decorators.",
            "To apply decorators to class methods."
          ],
          "answer": "To preserve the metadata of the original function when using decorators."
        },
        "level": "intermediate",
        "mark": 1,
        "time": 1
      },
      {
        "languageId": 2,
        "topicId": 46,
        "questions": {
          "question": "What is the purpose of a decorator factory in Python?",
          "code": "",
          "option": [
            "To create decorators dynamically with varying parameters.",
            "To remove decorators from functions.",
            "To apply decorators to class methods.",
            "To create decorators with fixed parameters."
          ],
          "answer": "To create decorators dynamically with varying parameters."
        },
        "level": "intermediate",
        "mark": 1,
        "time": 1
      },
      {
        "languageId": 2,
        "topicId": 46,
        "questions": {
          "question": "Which of the following is a correct way to define a decorator with parameters in Python?",
          "code": "",
          "option": [
            "def my_decorator(param):",
            "def my_decorator(*args, **kwargs):",
            "def my_decorator(func):",
            "def my_decorator(@param):"
          ],
          "answer": "def my_decorator(param):"
        },
        "level": "intermediate",
        "mark": 1,
        "time": 1
      },
      {
        "languageId": 2,
        "topicId": 46,
        "questions": {
          "question": "What happens when multiple decorators are applied to a single function in Python?",
          "code": "",
          "option": [
            "Only the first decorator is applied.",
            "Only the last decorator is applied.",
            "All decorators are applied in the order they are listed.",
            "Decorators cannot be applied to the same function."
          ],
          "answer": "All decorators are applied in the order they are listed."
        },
        "level": "intermediate",
        "mark": 1,
        "time": 1
      }
  ]
}  