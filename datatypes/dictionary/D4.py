# IMPORTANT PROBLEM

# word count problem ( the repeated word in a sentence )
# 1. split
# if key value not in the dic
# add key into dic

line='cat car bat dog mango bat rat mango dog cat cat dog bat rat'
dic={}
data=line.split(' ')
for i in data:          # cat
    if i not in dic:    # cat=t
        dic[i]=1        # cat=1
    else:
        dic[i]+=1       #if present cat=2
print(dic)
