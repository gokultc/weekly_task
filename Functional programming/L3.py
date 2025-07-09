# 1. find all of the numbers from the 1 to 1000 that are divisible by 7
# 2. find all of the numbers from the 1 to 1000 that 3 in them
# 3. count the no of space in the string
# 4. count the no of vovels in the string
# 5. find all the words in a list that are less than 4 character
from os.path import split

string='practice list comprehension problem to drill your head'
# 1
lst=[i for i in range(1,1000) if i%7==0]
print(lst)

#2
lst=[i for i in range(1,1001) if '3' in str(i)]
print(lst)

# 3
data=string.split(' ')
lst=[i for i in string if i==' ']
print(len(lst))

# 4
v='aeiou'
lst=len([i for i in string if i in v])
print(lst)

# 5
data=string.split(' ')
lst=[i for i in data if len(i)<4]
print(lst)
