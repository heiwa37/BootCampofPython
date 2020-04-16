'''
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3
'''
import math

def volume_sphere(diameter):
    radius=diameter/2
    v_sphere= (4/3*math.pi * radius**3)
    return v_sphere

print('Program to calculate the volume of sphere! ')
data_input=int(input("Please enter the diameter of the sphere = "))
result=volume_sphere(data_input)
print("The volume of the sphere is {} with given diameter of {}".format(result,data_input))
