from os import remove

employee=['vibin', 'neethu', 'rahul', 'alan', 'aml', 'binu', 'teena', 'sooraj']

# Using the del method
del employee[0:3] # to remove from a range
print(employee)

# Using the remove method
employee.remove("alan") #remove one element
print(employee)

# Using the clear method
employee.clear() # this clear the data but never remove the list
print(employee)

# Using the del method
del employee # this to delete all list