#comparison operation return true or false
#boolean logic operator "and , or , not"
#control flow condition
#1-IF
num = 5 
if num ==5:
    print("num is five ",num)
else:
    print("not five")
    
#dont forget significant indentation in python
#Nested IF
#elif depend on value & conected with if so once if is done it wont execute elif
#in else not worry about value


#2-WhILE LOOP
#check statment till condition not true
n = 1
while n<5:
    print(n) #1234
    n+=1
    print(n) #12345
    
print(n) #5

#3-FOR LOOP

for i in range(5):  #0:end
    print(i) #0:4
    
for i in range(2,5) : #(start,end)
    print(i) #2:4
    
for i in range(0,7,2): #(start,end,step)
    print(i) #0,2,4,6


#for loop with string can be (loop over string indexes ,  loop over string characters)
name = "aya tarek"
for index in range(len(name)):
    print(index)
    
for char in name:
    print(char)
    
    
#break statment "when have some condition end loop"
mysum=0
for i in range(5,11,2):
    mysum +=i
    if mysum ==5:
        break
    
print(mysum)