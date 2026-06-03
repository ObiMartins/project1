#This is a single line comment

"""This is a multiline
comment in python"""

surname = "Obi"
first_name = "Chinedu"
middle_name = "Emeka"
age = 40
print(surname.upper() + ", " + first_name + " " 
+ middle_name)

#Variable reassignment
surname = "Okeke"

full_name = (surname.upper() + ", " + first_name + " " 
+ middle_name)
print(full_name)

print("======lowercase=======")
print(full_name.lower())
print("=====title=======")
print(full_name.casefold())