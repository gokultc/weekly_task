# empty list
# TO ADD AN ELEMENT

# 1) APPEND ()

lst=[]
lst.append(50)
lst.append(60)
print(lst)

# 2) EXTEND ()
# It is used when we need to add multiple number to the list
lst.extend([60,50,30,20,40])
print(lst)

# 3) INSERT()
# ADD AN ELEMENT INTO A PARTICULAR POSITION >> INSERT()
lst.insert(1,25) # (position,element)

