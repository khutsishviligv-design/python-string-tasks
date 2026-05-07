davaleba1:
countdown=int(input("გთხოვთ შეიყვანეთ დადებით მთელი რიცხვი:"))
while countdown >= 1:
    print(countdown)
    countdown-=1


davaleba2:
total = 0

while True:
    number = int(input("შეიყვანე მთელი რიცხვი: "))

    if number == 0:
        break

    total += number
print ( total)


davaleba3:

secret_number = 9

while True:
    guess = int(input("გამოიცანი საიდუმლო რიცხვი: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break

davaleba4:
text = input("შეიყვანე ტექსტი: ")

vowels = "aeiouAEIOU"
result = ""

for ch in text:
   
    if ch in vowels:
        continue

    result += ch

print("შედეგი:", result)

davaleba5:

for i in range(0,9):
 print (i)

 for i in range(5, 15):
     print(i)
 for i in range(0, 21,2):

         print(i)


for i in range(10, 0,-1):
     print(i)
