#Bisection search algorithm
#depend on 3 values high, low , med= (low+high)//2
print("please think of num between 0 and 100")
low = 0
high =100
medium = (low+high)//2
state = True

while state:
    print("Is your secret num" +str(medium))
    guess = input("Enter 'h' if guess is too high, Enter 'l' if guess is too low, Enter 'c' if guess is correct")
    if guess =='c':
        print("Game over your secret num is:"+ str(medium))
        state = False
    elif guess == 'h':
        high = medium 
        medium = (low+high)//2
    elif guess == 'l':
        low = medium 
        medium = (low+high)//2
    else :
        print("sorry i didint unerstand your input")
        

