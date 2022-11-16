""" age = 17

if age<18 :
    print("vous etes mineur")
elif age== 18 :
    print('vous etez un peu majeur ')
else :
    print("vous etez majeur")

i=1
while i<10:
        print(i)
        i=i+1
else :
        print(i,"\' est plus egale a 10")

# Les listes

fruits = ["Ananas" ,"Pomme", "Mangue","Avocat"]

for f in fruits :
    print(f)  


# Les tuples

fruits = {"Ananas" ,"Pomme", "Mangue","Avocat"}

for f in fruits :
    print(f)

# Le sets


fruits = {"Ananas" ,"Pomme", "Mangue","Avocat"}

for f in fruits :
    print(f)


Dictionnaires
 
students = {
    "name": "John",
    "age" : 21,
    "adress" : "Kamenge"
 }

students["age"]=18

print(students)


for s in students.values():
    print(s)


del students

print(students)

Fonctions


<<<<<<< HEAD
=======
# Fonctions


>>>>>>> 56aeb5cdde33533c76968d888560535fdd503cd3
def show_students(first_name,last_name):
    print("Hello, "+first_name+" "+last_name)

first_name=str(input("Veuiller saisir votre nom :")) 
last_name=str(input("Veuiller saisir votre prénom :"))

show_students(first_name,last_name) """
    

def multiplying():
    first_number=int(input("Veuiller saisir le 1er entier :")) 
    second_number=int(input("Veuiller saisir le 2eme entier :"))
    result=first_number*second_number
    print("La multiplication de ",first_number,"et ",second_number," est ",result)

multiplying()