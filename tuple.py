#Tuples:  defined by parantheses() & item seperated by comma , & contain any type of objects
tup = (1,'c',3,'aya')

#retrieving elements from tuple using index
print(tup[2])

# + operator add new object to tuple
tup2 = tup + ('tarek', 50)
print(tup2)

#can creat tuple without parantheses 
tup3 = 10,
print(type(tup3))

#tuples are immutable ,values can not change once they are created
#can overwrite whole tuple but can not change index value in existing tuple

#1-using tuple to swap values
x = 5
y = 7
(x,y) = (y,x)
print(x,y)

#2- using tuple to return more than one value from functions
def quotient_remainder(x,y):
     q = x//y
     r = x%y
     return(q,r)
 
print(quotient_remainder(15, 7))