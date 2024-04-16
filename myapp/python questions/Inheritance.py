{
    "questions":[
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is inheritance in Python?",
        "code": "",
        "option": [
          "A feature that allows a class to inherit attributes and methods from another class.",
          "A feature that allows a class to inherit only attributes from another class.",
          "A feature that allows a class to inherit only methods from another class.",
          "None of the above."
        ],
        "answer": "A feature that allows a class to inherit attributes and methods from another class."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "Which keyword is used to inherit a class in Python?",
        "code": "",
        "option": [
          "extend",
          "inherits",
          "inherit",
          "class"
        ],
        "answer": "extend"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the superclass also known as?",
        "code": "",
        "option": [
          "Child class",
          "Derived class",
          "Parent class",
          "Subclass"
        ],
        "answer": "Parent class"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "Which type of inheritance allows a class to inherit from multiple base classes?",
        "code": "",
        "option": [
          "Single inheritance",
          "Multiple inheritance",
          "Hierarchical inheritance",
          "Hybrid inheritance"
        ],
        "answer": "Multiple inheritance"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What happens if a class inherits from multiple classes with the same method name?",
        "code": "",
        "option": [
          "Python throws an error.",
          "It depends on the order of inheritance.",
          "Both methods are inherited and can be called explicitly.",
          "Only the method from the first class is inherited."
        ],
        "answer": "Both methods are inherited and can be called explicitly."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the method called when an object of a derived class is created?",
        "code": "",
        "option": [
          "__init__",
          "__new__",
          "__create__",
          "__construct__"
        ],
        "answer": "__init__"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "Which method is used to call the method of the superclass from the subclass?",
        "code": "",
        "option": [
          "super()",
          "superclass()",
          "parent()",
          "base()"
        ],
        "answer": "super()"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is method overriding in Python?",
        "code": "",
        "option": [
          "Creating a new method in the subclass with the same name as a method in the superclass.",
          "Calling a method of the superclass from the subclass.",
          "Inheriting methods from multiple base classes.",
          "None of the above."
        ],
        "answer": "Creating a new method in the subclass with the same name as a method in the superclass."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "Which keyword is used to prevent a method from being overridden in the subclass?",
        "code": "",
        "option": [
          "override",
          "final",
          "private",
          "protected"
        ],
        "answer": "final"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\nclass A:\n    def show(self):\n        print('A class method')\nclass B(A):\n    def show(self):\n        print('B class method')\nobj = B()\nobj.show()",
        "option": [
          "A class method",
          "B class method",
          "Both A class method and B class method",
          "Error: Method 'show' is ambiguous."
        ],
        "answer": "B class method"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\nclass A:\n    def __init__(self):\n        print('A constructor')\nclass B(A):\n    def __init__(self):\n        print('B constructor')\nobj = B()",
        "option": [
          "A constructor",
          "B constructor",
          "Both A constructor and B constructor",
          "Error: Constructor 'init' is ambiguous."
        ],
        "answer": "B constructor"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "Which type of inheritance occurs when a class inherits from a class, and that class inherits from another class?",
        "code": "",
        "option": [
          "Single inheritance",
          "Multiple inheritance",
          "Hierarchical inheritance",
          "Multilevel inheritance"
        ],
        "answer": "Multilevel inheritance"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\nclass A:\n    def show(self):\n        print('A class method')\nclass B(A):\n    def show(self):\n        super().show()\n        print('B class method')\nobj = B()\nobj.show()",
        "option": [
          "A class method",
          "B class method",
          "Both A class method and B class method",
          "Error: Method 'show' is ambiguous."
        ],
        "answer": "A class method\nB class method"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\nclass A:\n    def __init__(self):\n        print('A constructor')\nclass B(A):\n    def __init__(self):\n        super().__init__()\n        print('B constructor')\nobj = B()",
        "option": [
          "A constructor",
          "B constructor",
          "Both A constructor and B constructor",
          "Error: Constructor 'init' is ambiguous."
        ],
        "answer": "A constructor\nB constructor"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\nclass A:\n    def show(self):\n        print('A class method')\nclass B(A):\n    def show(self):\n        super(B, self).show()\n        print('B class method')\nobj = B()\nobj.show()",
        "option": [
          "A class method",
          "B class method",
          "Both A class method and B class method",
          "Error: Method 'show' is ambiguous."
        ],
        "answer": "A class method\nB class method"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\nclass A:\n    def show(self):\n        print('A class method')\nclass B(A):\n    def show(self):\n        A.show(self)\n        print('B class method')\nobj = B()\nobj.show()",
        "option": [
          "A class method",
          "B class method",
          "Both A class method and B class method",
          "Error: Method 'show' is ambiguous."
        ],
        "answer": "A class method\nB class method"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 42,
      "questions": {
        "question": "What is the output of the following code?",
        "code": "\nclass A:\n    def __init__(self):\n        print('A constructor')\nclass B(A):\n    def __init__(self):\n        A.__init__(self)\n        print('B constructor')\nobj = B()",
        "option": [
          "A constructor",
          "B constructor",
          "Both A constructor and B constructor",
          "Error: Constructor 'init' is ambiguous."
        ],
        "answer": "A constructor\nB constructor"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
        "languageId": 2,
        "topicId": 42,
        "questions": {
            "question": "Which keyword is used to access the attributes and methods of the superclass from the subclass in Python?",
            "code": "",
            "option": [
                "superclass",
                "parent",
                "super",
                "base"
            ],
            "answer": "super"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 2,
        "topicId": 42,
        "questions": {
            "question": "What is the term used to describe a class that inherits from another class in Python?",
            "code": "",
            "option": [
                "Parent class",
                "Base class",
                "Superclass",
                "Derived class"
            ],
            "answer": "Derived class"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    },
    {
        "languageId": 2,
        "topicId": 42,
        "questions": {
            "question": "What is the output of the following code?",
            "code": "\n\nclass A:\n    def show(self):\n        print('A class method')\n\nclass B(A):\n    pass\n\nobj = B()\nobj.show()",
            "option": [
                "A class method",
                "B class method",
                "AttributeError: 'B' object has no attribute 'show'",
                "TypeError: 'NoneType' object is not callable"
            ],
            "answer": "A class method"
        },
        "level": "beginner",
        "mark": 1,
        "time": 1
    }
    
  ]
}  