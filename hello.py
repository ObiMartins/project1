import requests
response = requests.get("https://www.google.com")
print(response.status_code)
#print(response.text)
print("hello, world")


#Welcome message

print("==========Student score===========")
score = int(input("Enter your score"))
if score >= 90:
    print("Grade is: A")
elif score >= 75:
    print("Grade is: B")
elif score >= 60:
    print("Grade is: C") 
elif score >= 50:
    print("Grade is: D")
else:
    print("Grade is: F")
