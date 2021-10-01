C=""
print ("Введите имя")
Name = str(input())
print ("Введите фамилию")
Surname = str(input())
print ("Введите год рождения")
Year = int(input())
print(Name, "_", Surname, "_", Year)
C=Name
Name=Surname
Surname=C
Year+=60
print(Name, "_", Surname, "_", Year)





