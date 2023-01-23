#Dictionaries {key:value}
#use key to access the value & key can be any immutable type
#initiate withy {} but indexing with []
#can contain diif type of keys&values but to make it meningful let all keys&values at same type
dic = {'aya':'a+','nada':'a'}

#Adding new entity(key_value pairs)
dic['samar']='b-'
print(dic)

#the in & not in operators works on key
#dont forget case sensitive
print('hany'in dic)

#Delete del[dic[key]]
del[dic['samar']]
print(dic)

# .keys() return all keys of dic in one list
# .values() return values of dic in one list
print(dic.keys())
print(dic.values())

#can also use get to return value of key
print(dic.get('aya'))
print(dic.get('hany')) #dosent get error if key not exist but if using index you will get error
print(dic.get('salma','not exist'))  #get(key,value if key dose not exist)

# .update()
dic2 = {'soma':'c-','rana':'b'}
dic.update(dic2)
print(dic)