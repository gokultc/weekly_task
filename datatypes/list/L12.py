# SLICING
# important interview question


lst=[1,3,5,6,7,4,8,9,3,8]

# INDEXING
print(lst[4])
print(lst[1])
print(lst[0])

# SLICING is applied in the to get a range of the element from the list
# SLICING only works from left to right
# [start:stop]

print(lst[2:5]) # ind=2,3,4  out=5,6,7

print(lst[4:])  # it will start from the 4th and end in the last of the list

print(lst[:5]) # in this it will print from the first to 5 th element

print(lst[2:7:2]) # [start:stop:step]

print(lst[2::2]) # 2,4,6,8,

# NEGATIVE INDEXING

# -1 TO -N

print(lst[-1]) # 8

print(lst[-6]) # 7