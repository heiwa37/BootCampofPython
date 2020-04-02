if __name__ == '__main__':
    while True:
        try:
            num1=10
            num2=input("please enter the second number")
            num2= int(num2) # the output is string and int ; so we cannot add
            result= num1+num2
            print("the output is : {}".format(result))
        except:
            print("I think issue in the try block. check again please!")
            continue
        else:
            print("the program worked!")
            break
        finally:
            print("I will always run no matter what exception")
