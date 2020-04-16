'''
2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
'''

input=['x','y','z']
output=[i*j for i in input for j in range(1,5)]
print(output)

input=['x','y','z']
output=[i*j for i in range(1,5) for j in input]
print(output)

input_list=[2,3,4]
output=[[i+num] for i in input_list for num in range(0,3)]
print(output)

input_list=[2,3,4,5]
output=[i+num for i in input_list for num in range(0,4)]
print(str(output))


input=[1,2,3]
output=[(j,i) for i in input for j in input]
print(output)
