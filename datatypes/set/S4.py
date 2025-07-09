# SET OPERATIONS

#1. UNION

#2. INTERSECTION

#3. DIFFERENCE

st1={1,2,3,4,5,6,7,8}
st2={5,6,7,10,20,30,40,50,60,70,80}

# Union - combined results of two sets are produced
st3=st1.union(st2)
print(st3)


# Intersecion - collects the common elements
st3=st1.intersection(st2)
print(st3)

# difference -

# A-B = element present in A but not in B
st4=st1.difference(st2)
print(st4)

# B-A = element present in B but not in Ast4=st1.difference(st2)
st5=st2.difference(st1)
print(st5)

