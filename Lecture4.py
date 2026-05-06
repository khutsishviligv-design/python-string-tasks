""1. მომხმარებელს შემოატანინე ასაკი (input() გამოყენებით) და if / elif / else გამოყენებით დაადგინე, რომელი კატეგორიას ეკუთვნის:
ბავშვი (0–12)
თინეიჯერი (13–19)
ზრდასრული (20–64)
უფროსი (65+)
ბოლოს დაბეჭდე შედეგი, მაგალითად:
"თქვენ ხართ: თინეიჯერი"""

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
