#!/usr/bin/env python3
#this is a single line comment
#python programme to illusrate operators in python
#name :Marvin Kinyanjui
#email :kinyanjuip249@gmail.com
#Date :17th Feb2023
#file :operators.py
#!/usr/bin/en/python3
#create an empty list of favourite musicians
#Using for loop add atleast 5 new musicians
#Copy the least of favourite musicians
#sort the list
#pop out two celebrities from the list
#count the remaining celebs

favourite_musicians1 = ["Pop Smoke","Juice World"," Ben githae","Shiro wa Gp","Kenny Rogers","Flourida georgia"]
print(favourite_musicians1)
print("-----------------")

favourite_musicians2=["size 8","short baba","bahati","mabel","g-eazy"]
print(favourite_musicians2)

for musicians in favourite_musicians2:
    favourite_musicians1.append(musicians)
print(favourite_musicians1)

favourite_musicians1.copy()
print(favourite_musicians1)

favourite_musicians1.sort()
print(favourite_musicians1)

favourite_musicians1.pop()
print(favourite_musicians1)

favourite_musicians1.pop()
print(favourite_musicians1)

favourite_musicians1.count(6)
print(favourite_musicians1)













