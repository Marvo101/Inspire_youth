#!/usr/bin/env python3
#this is a single line comment
#python programme to illusrate operators in python
#name :Marvin Kinyanjui
#email :kinyanjuip249@gmail.com
#Date :17th Feb2023
#file :operators.py
#!/usr/bin/en/python3

my_favourite_fruits=["banana","mango","apple","watermelon","avocado"]
for fruit in my_favourite_fruits:
    print(fruit)

    #len number of elements in the list
    print(len(my_favourite_fruits))

friends=["Gloria","Lydia","Faith","Wilma","Travis"]
print(friends)
friends[0]="Mary"
print(friends)
print("----------------")
new_friends=friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)