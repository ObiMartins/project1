
#Calculate the total price of 3 items using multiplication and addition.
num1 = 10
num2 = 20
num3 = 30
print((num1 * num2) + num3)
print("====================================")

#Create age and has_license variables, then check if the person can drive
age = 30
has_license = True
if (age >= 30 and has_license):
    print("You can drive")
else:
    print("You are not of age")

print("====================================")

#Use and, or, and not in three separate examples.
is_boy = True
is_girl = True
is_adult = False
human = is_boy and is_girl
teeneger = not is_adult
precious_gift = is_boy or is_girl
print(human)
print(teeneger)
print(precious_gift)