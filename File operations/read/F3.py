f=open('/File operations/numberes', 'r')
lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))
print(lst)
print(sum(lst))

# rstrip() -  To remove a character from the right string
# lstrip() -  To remove a character from the left string

# if the output contains any /n we can use the rstrip method to remove it from the right side
# Example
# data='hello/n'
# data1=data.rstrip('/n')
# print(data1)