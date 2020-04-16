'''
create a pattern below:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
try:
    data_len=int(input("Print the number of rows to be printed on the pattern: "))
    for i in range(0,data_len):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
    for i in range(data_len,0,-1):
        for j in range(0,i-1):
            print("*",end=" ")
        print("\r")
except ValueError:
    print("\nInvalid data format! Please Enter Integer number")
