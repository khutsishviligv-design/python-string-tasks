#davaleba1
list=[10,2,3,4,5]
total=0
for i in list:
 total+=i
 print (total)


# davaleba2
nums = [10, 2, 3, 4, 5]

a = sorted(nums)

print("min:", a[0])
print("max:", a[-1])

#davaleba3

numbers = [10, 2, 3, 4, 5, 11, 8, 7]


even_numbers = []
odd_numbers = []


for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("even:", even_numbers)
print("odd:", odd_numbers)

#davaleba4
list=[1,2,3,5]
print(tuple(list))
print(list)

#davaleba5:
all_numbers=[3,4,5,6,5,6,7]
clean_number=[]

for i in all_numbers:
  if i not in clean_number:
   clean_number.append(i)
print(clean_number)
