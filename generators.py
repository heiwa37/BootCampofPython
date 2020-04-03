'''
Generators:function allows us to write a funtion that can send back a value from where we left off
and later pick up from where we left off
- allows us to Generate sequence of numbers overtime
- syntax will be different
    keyword- yield
'''
#cube given number

def cube_number(n):
    for x in range(n):
        yield (x**3)

print(cube_number(10))
for i in cube_number(100):
    print(i) # it doesn't store in memory
# or another way
print(list(cube_number(10))) # converting to list but it stores into memory

########################################################################################################
# fibonacci series

def fibo(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        #print("the a value is: ",a)
        a, b = b ,a+b

for number in fibo(10):
    print(number)
