#objects in python can be (scaler , non-scaler)
#scaler can not be subdivided
#non-scaler has internal structure that can be accessed 

#scaler
x = int(7)
print(x)
print(type(x))

y = float(9)
print(y)
print(type(y))
b = bool(True)
print(b)
print(type(b))

#expression :  object + operator + object "ordered operation"
 
x = (5+6)*7
print(x)

#how to name variables in python
#names should be descriptive
#avoid using python keywords 
#variables are case sensitive

#non-scaler
#strings
name1 = "aya"
name2 = "tarek"
#in string 
#+ means concatenation
#* means replication

print(name1+name2)
print(name1*5)

#len() num of characters in string
print(len(name1))

#use indeexing in strings start from 0 : l-1
print(name2[0])

#slcing return substring of string [start:stop] "execlesive"
#make  sure you dont accesses any index out of range
print(name2[0:2])
#can use  step in slicing [start:stop:step]
print(name2[0:4:2])
#to reverse all string use [::-1]

#in operatir to check if caracter in string or not
print("ta" in name2)


#input() function wait for user to enter text "take one argument prompot or instraction to let user know what to do"
#input() return string by defult , to overcome it you can
c = int(input("Enter integer"))
print(type(c))