#advanced data types

#mutable vs immutable

#mutable are data types that can be changed / edited during programmes life cycle
#add / remove elements
#immutable are data types that can't be changed / edited during programmes life cycle

#list (mutable)
friends=["Travo","Lydia" "Gloria","Faith"]
#friends[] for empty list
#add---->append(),extend()
students=["Albert","Rita","Precious"]

friends.extend(students)
friends.append(students)
friends.sort()
friends.reverse()
#tuples(immutable)
#types of list that are immutable
stationary=("pens","ink","steplar")
#you can replace the whole tuple
stationaries=("ruler","clipboerd")

for stationaries in stationary:
    print(stationary)

    numbers=(1,2,4,6,7,8,9)

#dictionaries aka dict

#use key and value pair to store data

student ={"name":"Bob","age" :24,"gender" :"male","is_tall":True}

print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])
#sets

#dictionaries aka dict
friends={"Travo"}
print(friends)
fav_colour={"red"}
print(fav_colour)
hobby={"playing play station"}
print(hobby)
course={"engineering"}
print(course)
weight={"60 kgs"}
print(weight)
height={"5 feet"}
print(height)
print(student.values)
print(student.keys)