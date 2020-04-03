'''
iter is the keyword which can be used to iterator the string or numbers
'''

s= 'hello'
for i in s:
    print(i)

print("*******")

str=iter(s)
print(str) # returns object
print(next(str)) # h
print(next(str)) # e
print(next(str)) # l
print(next(str)) #l
print(next(str)) # o
#print(next(str)) # #give error cause stop iterator
