#davaleba1
lst=["Monkey","Snake","Dog","Dog","Cat","Cat"]


values={}

for i in lst:
    if i in values:
        values[i] += 1
    else:
        values[i]=1
print(values)


#davaleba2
dict1={"Name":"Giorgi","age":19}
dict2={"Name":"Ana"}
dict3={}
lst=[]
for key, values in dict1.items():
    if key in dict2.keys():
        lst.append(dict2[key])
        lst.append(dict1[key])

dict3["Name"]=lst

print(dict3)

#davaleba3
dict={'a': 1, 'b': 2, 'c': 3}
reve={}

for key, values in dict.items():
    reve[values]=key
print(reve)


#davaleba4:
films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}

saertofilmebi= films1.intersection(films2)
pirveliadamiani=films1.difference(films2)
meoreadamiani=films2.difference(films1)
unicfilms=films1.union(films2)

print(f': saertofilmebi:{saertofilmebi}')
print(f': pirveliadamiani:{pirveliadamiani}')
print(f': meoreadamiani:{meoreadamiani}')
print(f':uniquefilms:{unicfilms}')

#davaleba5:


#5.1
for name, data in info_full["კლასი 10A"].items():
    sashualo=name, data["საშუალო_ქულა"]

    print(sashualo)

#5.2
max_qul=0
for name , data in info_full["კლასი 10A"].items():
    qulebi=data["საშუალო_ქულა"]
    if qulebi > max_qul:
        max_qul = qulebi
        best_student=name

print (max_qul,best_student)

#5.3

for class_name ,students in info_full.items():
    for name, data in students.items():
        dastsreba=data["დასწრება"]
        if dastsreba>90:
            print(name,dastsreba)

#5.4
max_count=0
maxclass_name=""
for class_name ,students in info_full.items():

        count=len(students)
        if count >max_count:
            max_count = count
            maxclass_name=class_name

            print ("bevri studenti", max_count, "aris", maxclass_name, "shi")


#5.5
programireba="პროგრამირება"
for students_name, data in info_full.items():
    for student, programs in data.items():
       if programireba in programs["დამატებითი"]:
         print (student)


#5.6


total = 0
count = 0

for students_name, data in info_full.items():
    for student, dastsreba in data.items():
        total+=dastsreba["დასწრება"]
        count+=1
        average_attendance = total / count
print (average_attendance)

#5.7
dicti={}
for stundet_name, data in info_full.items():
    for student, sagnebi in data.items():
        count=len(sagnebi["საგნები"])
        dicti[student]=count
print (dicti)


#5.8

max_activities = 0
best_student = None
best_class = None

for class_name, students in info_full.items():
    for student_name, data in students.items():
        activities_count = len(data["დამატებითი"])

        if activities_count > max_activities:
            max_activities = activities_count
            best_student = student_name
            best_class = class_name

print("აქტივობების რაოდენობა", max_activities,best_student)
