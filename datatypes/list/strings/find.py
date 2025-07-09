# find method
# index method

s2='my name is gokul'
print(s2.find("is")) #8
print(s2.index("is")) #8

print(s2.find("hello")) # -1
# # will show value error


#rfind method
s='my name is gokul.is it okey.is'
print(s.rfind("is")) #28 is the output
# in this rfind() the output if find from the last

print(s.count("is")) #will find the no of is in it (3)
