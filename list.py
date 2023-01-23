#lists: denoted by square brackets []
#can contain mixed types but better to only contain homogeneous elements
#lists are mutable

l1 = [1,2,3,4,5]
print(l1)

# .append(item) to add 1 item at end of list
l1.append(6)
print(l1)

# .extend(list) add list of items
l1.extend([7,8])

#del(list[index]) delet element at spacific index
del(l1[3])
print(l1)

# .remove() remove spacific element "if element occure multiple times, remove firist element & rasis ValueError if there is no such element"
l1.remove(1)
print(l1)

# .pop(index) remove & return indexed element of list if you do not spacify index it remove&return last element
x = l1.pop()

#you can convert string to list using list(string) or using .split()
s = 'aya tarek'
l2 = list(s)
print(l2)

l3 = s.split(" ")
print(l3)

#concatinating list into string using .join(list)
s2 = ' '.join(l3)
print(s2)

#sorted(list) return sorted list but not mutate/order list
print(sorted(l1))

# list.sort() mutates & sort items of list
l1.sort() 
print(l1)
# list.reverse() reverse elements of list in place
l1.reverse() 
print(l1)

#Alise list
l6 = [1,2,3] 
l7 = [1,2,3]
#both have same variables but store in diff place in  memory

l8 = l7 #now both in same memory place any change on anyone of them change oon another

l8[1] = 6
print(l7,l8)


l9 = [5,0,8]
l0 = l9.sort()
print(l9)
print(l0) #none

#if you want to fill list use sorted(list)
l0 = sorted(l9)
print(l0)

#Mutation and Iteration 
#dont make iteration on list that you change on lenght of
#function to remove duples between two lists
list1 = [1,2,3,4,5,6]
list2 = [2,4]
list1_copy = list1
def remove_duples(l1,l2):
    for e in list1_copy: #if you want to make iteration on changed lenght list , take copy of it and make iteration on copy not list
        if e in l2:
            l1.remove(e)
            
remove_duples(list1, list2)
print(list1)