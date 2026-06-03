import datetime
import os
import json
today = datetime.date.today()
print(today)

current_user = os.getcwd()
print(current_user)

data = {"Name": "Python", "age": 30, }
json_string = json.dumps(data)

print(json_string)

result = data["age"]
print(f"result. {result}")


