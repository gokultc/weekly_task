# to collect value from a dictionary we use the corresponding key
# value ==>> key

dic={'id':101,'name':'gokul tc','age':21,'prof':'bigdata','salary':50000}
print(dic)

print(dic['age'])
print(dic['salary'])

# To collect values from dic seperatly we use dic[i]
for i in dic:
    print(i,':',dic[i])

# MUTABLE
# To update value we key value
dic['age']=30
dic['prof']='python'
dic['salary']+=500
print(dic)

# To add new key-value pair
dic['location']='ekm'

# to find new a value
print('age' in dic)

print('salary' in dic)

print('home' in dic)

# TO DELETE element from the dictionary
del dic['age']
print(dic)