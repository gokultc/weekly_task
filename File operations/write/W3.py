# read a file and write the file without the apple

f=open('fruits','r')
s=open('new_fruits','w')
for i in f:
    if 'apple' not in i:
        s.write(i)