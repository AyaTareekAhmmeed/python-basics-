#use functions for repeated code with same functionality 
#provide less peace of code + more functionality

#1- No Arguments & No return 
def printHello():
    print("Hello Aya")
    
#to execute function juest call it using function name
printHello()

#2-with Arguments & No return
def printSum(num1,num2):
    print(num1+num2)
    
printSum(50, 30)

#3-No arguments & return
def pi():
    return 22/7

circ = 2*7 *pi()
print(circ)

#4-with Arguments & return
def isEven(num):
    return num%2 == 0

print(isEven(5))

#variable scope (Global scope: main body off script , Formal scope: define inside function)
#EX1
def f(y):
    x=1
    x+=1
    print(x)

x=5
f(x)
print(x)

#EX2
def g(y):
    print(z)
    print(z+1)
    
z=5
g(z)
print(z)

#EX3 "error" you cant creat variable and use it without initialization in function scope even if it was initialized in global
def h(y):
    x = x +1
    
h(x)
print(x)
    