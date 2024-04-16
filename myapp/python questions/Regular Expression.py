{
    "questions":[
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is a regular expression?",
        "code": "",
        "option": [
          "A sequence of characters that forms a search pattern.",
          "A built-in function in Python for searching and manipulating strings.",
          "A type of list in Python used for storing sequences of elements.",
          "A method used for iterating over characters in a string."
        ],
        "answer": "A sequence of characters that forms a search pattern."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "Which module in Python is used for working with regular expressions?",
        "code": "",
        "option": [
          "os",
          "re",
          "sys",
          "math"
        ],
        "answer": "re"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What does the function `re.search()` do?",
        "code": "",
        "option": [
          "It searches for a specified pattern within a string.",
          "It returns a match object if there is a match anywhere in the string.",
          "It checks if the string starts with the specified pattern.",
          "It replaces occurrences of the specified pattern with a new string."
        ],
        "answer": "It searches for a specified pattern within a string."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is the result of the following code snippet?",
        "code": "\nimport re\npattern = r'apple'\nresult = re.match(pattern, 'apple pie')\nprint(result.group())",
        "option": [
          "apple",
          "pie",
          "apple pie",
          "None"
        ],
        "answer": "apple"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What does the function `re.findall()` do?",
        "code": "",
        "option": [
          "It searches for a specified pattern within a string and returns the first occurrence.",
          "It returns a list of all occurrences of the specified pattern in the string.",
          "It checks if the string contains the specified pattern.",
          "It replaces all occurrences of the specified pattern with a new string."
        ],
        "answer": "It returns a list of all occurrences of the specified pattern in the string."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "Which metacharacter in regular expressions matches any single character except newline characters?",
        "code": "",
        "option": [
          ".",
          "*",
          "^",
          "$"
        ],
        "answer": "."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is the result of the following code snippet?",
        "code": "\nimport re\npattern = r'ba*'\nresult = re.findall(pattern, 'baaaa')\nprint(result)",
        "option": [
          "['b', 'a', 'a', 'a', 'a']",
          "['b', 'a*']",
          "['b', 'aa', 'a']",
          "['b', 'aa']"
        ],
        "answer": "['b', 'aa', 'a']"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What does the character '^' represent in regular expressions?",
        "code": "",
        "option": [
          "It matches the start of a string.",
          "It matches the end of a string.",
          "It matches zero or more occurrences of the preceding character.",
          "It matches one or more occurrences of the preceding character."
        ],
        "answer": "It matches the start of a string."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is the result of the following code snippet?",
        "code": "\nimport re\npattern = r'\\d+'\nresult = re.findall(pattern, 'There are 123 cats and 456 dogs')\nprint(result)",
        "option": [
          "['123', '456']",
          "['1', '2', '3', '4', '5', '6']",
          "['1', '123', '456']",
          "['123 cats', '456 dogs']"
        ],
        "answer": "['123', '456']"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What does the character '$' represent in regular expressions?",
        "code": "",
        "option": [
          "It matches the start of a string.",
          "It matches the end of a string.",
          "It matches zero or more occurrences of the preceding character.",
          "It matches one or more occurrences of the preceding character."
        ],
        "answer": "It matches the end of a string."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "Which function is used to replace occurrences of a pattern in a string with another string in regular expressions?",
        "code": "",
        "option": [
          "re.replace()",
          "re.sub()",
          "re.match()",
          "re.find()"
        ],
        "answer": "re.sub()"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is the result of the following code snippet?",
        "code": "\nimport re\npattern = r'\\s'\nresult = re.split(pattern, 'apple orange banana')\nprint(result)",
        "option": [
          "['apple', 'orange', 'banana']",
          "['apple orange banana']",
          "['a', 'p', 'p', 'l', 'e', 'o', 'r', 'a', 'n', 'g', 'e', 'b', 'a', 'n', 'a', 'n', 'a']",
          "['a', 'pple', 'o', 'range', 'b', 'anana']"
        ],
        "answer": "['apple', 'orange', 'banana']"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What does the character '+' represent in regular expressions?",
        "code": "",
        "option": [
          "It matches the start of a string.",
          "It matches the end of a string.",
          "It matches zero or more occurrences of the preceding character.",
          "It matches one or more occurrences of the preceding character."
        ],
        "answer": "It matches one or more occurrences of the preceding character."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is the result of the following code snippet?",
        "code": "\nimport re\npattern = r'\bcat\b'\nresult = re.search(pattern, 'The cat is black')\nprint(result.group())",
        "option": [
          "cat",
          "The cat is black",
          "black",
          "None"
        ],
        "answer": "cat"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What does the character '*' represent in regular expressions?",
        "code": "",
        "option": [
          "It matches the start of a string.",
          "It matches the end of a string.",
          "It matches zero or more occurrences of the preceding character.",
          "It matches one or more occurrences of the preceding character."
        ],
        "answer": "It matches zero or more occurrences of the preceding character."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is the result of the following code snippet?",
        "code": "\nimport re\npattern = r'[aeiou]'\nresult = re.findall(pattern, 'apple orange banana')\nprint(result)",
        "option": [
          "['a', 'e', 'o', 'a', 'e', 'a', 'a', 'a']",
          "['a', 'e', 'i', 'o', 'u']",
          "['a', 'o', 'a', 'o', 'a', 'a']",
          "['apple', 'orange', 'banana']"
        ],
        "answer": "['a', 'e', 'o', 'a', 'e', 'a', 'a', 'a']"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is the result of the following code snippet?",
        "code": "\nimport re\npattern = r'[0-9]'\nresult = re.findall(pattern, 'There are 123 cats and 456 dogs')\nprint(result)",
        "option": [
          "['1', '2', '3', '4', '5', '6']",
          "['123', '456']",
          "['1', '123', '456']",
          "['123 cats', '456 dogs']"
        ],
        "answer": "['1', '2', '3', '4', '5', '6']"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What is the result of the following code snippet?",
        "code": "\nimport re\npattern = r'^The'\nresult = re.findall(pattern, 'The cat is black')\nprint(result)",
        "option": [
          "['The']",
          "['The cat']",
          "['cat']",
          "None"
        ],
        "answer": "['The']"
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    },
    {
      "languageId": 2,
      "topicId": 45,
      "questions": {
        "question": "What does the function `re.fullmatch()` do?",
        "code": "",
        "option": [
          "It searches for a specified pattern within a string.",
          "It returns a match object if the entire string matches the specified pattern.",
          "It replaces occurrences of the specified pattern with a new string.",
          "It checks if the string starts with the specified pattern."
        ],
        "answer": "It returns a match object if the entire string matches the specified pattern."
      },
      "level": "beginner",
      "mark": 1,
      "time": 1
    }
  ]
}  