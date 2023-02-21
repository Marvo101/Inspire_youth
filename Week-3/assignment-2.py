#!/usr/bin/env python3
#this is a single line comment
#python programme to illusrate operators in python
#name :Marvin Kinyanjui
#email :kinyanjuip249@gmail.com
#Date :17th Feb2023
#file :operators.py
#!/usr/bin/en/python3
#write a programme solving quandratic equation
#using for loop draw a diamond,triangle and a pascal's triangle

#programme soloving quandratic equation
 
import cmath

first_coefficient=int(input("Enter the first coefficient:"))
second_coefficient=int(input("Enter the second coefficient:"))
constant=int(input ("enter the constant:"))

a="coefficient of the first term"
b="coefficient of the second term"
c="constant"

ans1= -b(second_coefficient) + cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)
ans2= -b(second_coefficient) - cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)

print("The answers are"+str(ans1)+"and"+str(ans2))

#using a for loop to draw a diamond
R=int(input("Enter the range:"))
for diamond in range(R):
    print("  " * (R - diamond)," *" * (2 * diamond +1))
                                           
print("--------------------------")

#using  a for loop draw a triangle
for triangle in range(b,H):
    print("1/2" * (b - triangle) * (H -triangle))

    print("-----------------------")

#Drwaing pascals triangle using a for loop
for i in range(1,R+1):
    for j in range(0,R-i+1):
        print('',end='')

#first element is always 1
c=1
for j in range(1,i+1):

    #first value in a line is always 1
    print('',c,sep='',end='')

    #using binomial coefficientS
    c=c * (i-j) // j
    print()