'''
Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name.
'''
first_name=input("Please enter your First name = ")
last_name=input("Please enter your last name = ")
if(first_name.isdigit() | last_name.isdigit()):
    print("Numbers are not allowed! Please enter your Name!")
else:
    print("The given name is printed in reverse order : {last_name} {first_name}".format(last_name=last_name,first_name=first_name))
