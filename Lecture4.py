

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
