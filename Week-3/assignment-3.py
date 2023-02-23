#write a programme to print the factorial of a number using functions
#write a programme to calculate simple interest
#SI=(P * R * T)/100
#a programme of printing the factorial of numbers using functions
def factorial(n):
    for i in range (0,n):
        fact_n=n * (n-i)
        return fact_n

print(factorial(12))
print(factorial(11))
print(factorial(10))
print(factorial(9))
print(factorial(8))
print(factorial(7))
print(factorial(6))
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))

#a programme of calculating the simple interest
P=("Enter the principal amount")
R=("Enter the rate")
T=("Enter the time/period in years")
SI=((str(P)*str(R)*str(T))/100)
P=100000
R=15
T=2
print(P)
print(R)
print(T)
print(SI)

def SI(str(P,R,T)/100):
    simple_interest=P*R*T
    print(SI)
#calling/invoking the function
#print_name
SI(50000,15,2) #pass the parameters
