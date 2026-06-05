
#Create one integer, one float, one string, and one boolean.
age = 20
money = 20.55
name = "Obi Martins"
is_adult = True
print("======Concatenation with data types=============")
print("It is " + str(is_adult) + " that " + name + " is " + str(age) +
       " years old and has $" + str(money) + " in bank.")

#Use type() to print the type of each value.
print("======Printing data types============")
print(type(age))
print(type(money))
print(type(is_adult))

#Create a variable age = "25" as text, then convert it to a number and add 5
num_2 = "25"
print(int(num_2) * 5 )

#Write two boolean comparisons using your age or score.
score = 100
age = 40
is_excellent = True
is_adult = True
if (score >= 100 and is_adult):
    print("Congratulations! You are qualified for a scholarship")
else:
    print("Sorry! You are not qualified for a scholarship")

        
