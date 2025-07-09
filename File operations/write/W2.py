# copy paste the data from one file to another

f=open('C:/Users/GOKUL/PycharmProjects/may_datascience/File operations/write/write_data','r') # current file
w=open('new_write','w') # creating new file
for i in f:
    w.write(i) # writing the data in the i to the w file