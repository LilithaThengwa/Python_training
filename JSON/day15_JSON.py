import json
from pprint import pprint

data = {
    "employees": [
        {"name": "Alice", "age": 30, "department": "Sales"},
        {"name": "Bob", "age": 25, "department": "Marketing"},
    ]
}

# print(type(data))
# print(data["employees"][0]["age"])

data_json = json.dumps(data, indent=4)

# print(data_json, type(data_json)) # type of string. print(data_json["employees"]) throws an error.

student_json = """
        {
            "name": "gemma",
            "gender": "female"
        }
"""


# JSON --> Javascript Object Notation - string
student = json.loads(student_json) # Json to dictionary
# print(student["name"])

#First-Class Function --> Funtion treated as a value.
sport = {"name": "Dhoni", "dbl": lambda x: x * 2} #valid dictionary
# print(sport["dbl"](100))

# sport_json = json.dumps(sport) # JSON serializable (Convert) | Can't convert dict because it contains a function.
# print(sport_json) # Invalid JSON

# ====================================================================================================================

# task 1


bank_data = '''
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
'''

bank_list = json.loads(bank_data)
# for user in bank_list:
#     if (user["isActive"]):
#         user["balance"] += (user["balance"] * 0.1)
# result = json.dumps(bank_list, indent = 4)

result = [user.update({'balance': user['balance'] + (user['balance'] * 0.1)}) for user in bank_list if (user["isActive"])]
# result = json.dumps(bank_list, indent = 4)

# pprint(result)

# ===============================================================================================================================================

# convert to file. open to create, read a file. W and R stand for read and write. With for silent error handling.
# with open("bank_accounts.json", "w") as file:
#     json.dump(result, file, indent = 4)

# read
# with open("bank_accounts.json", "r") as file:
#     data = json.load(file)
    # print(data, type(data))

#===================================================================================================================================================

dict = {
  "posts": [
    {
      "title": "The Future of AI",
      "author": "Alice",
      "published_date": "2024-01-01",
      "comments": [
        {
          "user": "Bob",
          "comment": "Great post!",
          "date": "2024-01-02"
        },
        {
          "user": "Charlie",
          "comment": "Very informative.",
          "date": "2024-01-03"
        }
      ]
    },
    {
      "title": "Learning Python",
      "author": "Bob",
      "published_date": "2024-02-15",
      "comments": [
        {
          "user": "Alice",
          "comment": "Thanks for the tips.",
          "date": "2024-02-16"
        }
      ]
    },
    {
      "title": "Web Development Trends",
      "author": "Charlie",
      "published_date": "2024-03-01",
      "comments": []
    }
  ]
}

# with open("blog_post.json", "w") as file:
#     json.dump(dict, file, indent = 4)

# summary_list = []

# with open("blog_post.json", "r") as file:
#   read_data = json.load(file)
#   # for post in read_data["posts"]:
#   #     summary = {"title": post["title"], "author": post["author"],
#   #     "number_of_comments": len(post["comments"])}
#   #     summary_list.append(summary)

with open("blog_post.json", "w") as file:
    json.dump(dict, file, indent = 4)

with open("blog_post.json", "r") as file:
  read_data = json.load(file)
  
summary_dict = [{"title": post["title"], "author": post["author"], "number_of_comments": len(post["comments"])}
           for post in read_data["posts"]]

final_result = {"posts_summary": summary_dict}

with open("post_summary.json", "w") as file:
    json.dump(final_result, file, indent = 4)

# {
#   "posts_summary": [
#     {
#       "title": "The Future of AI",
#       "author": "Alice",
#       "number_of_comments": 3
#     },
#     {
#       "title": "Learning Python",
#       "author": "Bob",
#       "number_of_comments": 1
#     },
#     {
#       "title": "Web Development Trends",
#       "author": "Charlie",
#       "number_of_comments": 0
#     }
#   ]
# }
 