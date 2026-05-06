

"davaleba1"
age=int(input("Please enter your age:"))
if age  >=0 and age <=12:
    status="Child"
elif age >=13 and age <=19:
    status="Teenager"
elif age >= 20 and age <= 64:
    status="Adult"
elif age >= 65:
    status = "Senior"
else:
    status = "not correct age"

print("You are:", status)



"davaleba2"
score= int(input("Hello Student, what is your score"))
attendance= int(input("What was your attendance in percentage? (%)"))
if score >= 60 and attendance >= 75:
    print ("You pass")
else:
    print("You fail")



"davaleba3"
student_y_n=input("Are you student y/n?:")
member_y_n= input("Are you member y/n?:")
if student_y_n == "y" and member_y_n == "y":
    print ("you have addtional discount")
elif student_y_n == "y" or member_y_n == "y":
    print("you have discount")
else:
    print("sorry you dont have dicount")



"davaleba4"

username = input("eneter username: ")

if 3 <= len(username) <= 20 and username.isalnum():
    print("username correct")
else:
    print("username wrong")

