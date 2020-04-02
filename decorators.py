def func(some_other_func):
    def wrap_func():
        print("some random lines of code befoer it calls function")
        some_other_func()
        print("Some other final codes")
    return wrap_func

@func
def myfunc():
    print(" \t just i'm being called inside wrap_func")

new_function=func(myfunc)
print(new_function) # it just prints  object but not contents
print(new_function())

print("*********************************")

#using Decorator operator @
 # we can use @ operator of what function need to be Decoratored under new new_function and call that func
 
print(myfunc())
