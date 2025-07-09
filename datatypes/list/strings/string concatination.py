#string concatination is a method of combining multiple strings

#STRING CONCATINATION USING  + operator
str1='python'
str2='programming'
print(str1+' '+str2)

#STRING CONCATINATION USING join() method

x='python'
y='programming'
print("".join([x,y]))
print("_".join([x,y]))
print(" ".join([x,y]))
# in this the values insterted in the double will be used to join the words


#STRING CONCATINATION USING % method
a='hello'
b='welcome'
print("%s%s" %(a,b))
print("%s_%s" %(a,b))
print("%s   %s" %(a,b))
# in between 2 %s we can add space


##STRING CONCATINATION USING format() method
p="hello"
q="welcome"
print("{} {}".format(p, q))

#STRING CONCATINATION USING comma ,
print(p,q)
