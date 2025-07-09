# BINARY SEARCH

#lst=[4,5,6,2,3,12,15,10,8]

#1. Sort the given list
#ascending order [2,3,4,5,6,8,10,12,15]
#                low              upper

#2. Variable declare
# low=0
# upper=len(lst)-1       9-1=8

#3. Calculate the mid
# mid=(low+upper)//2      (0+8)//2=4

# 3 conditions

# A. element>lst[mid]           right side of the list
#       low=mid+1

# B. element<lst[mid]           Left side of the list
#       upper=mid-1

# C. element==lst[mid]
#        element found