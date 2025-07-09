#1. create a list of square of numbers from 1 to 10

#2. Create a list of even numbers from 1 to 20

#3. Generate a list of characters from a string

string='Helloworld'

#4. create a list of lengths of words in a sentence

string1='this is a sample sentence'

#5. create a list of common multiples of 3 and 5 upto 100

#6. create a list of reversed strings from another list

words=['apple','orange','mango']

# 1
lst=[i**2 for i in range(1,11)]
print(lst)

# 2
lst=[i for i in range(1,21) if i%2==0]
print(lst)

# 3
lst=[i for i in string]
print(len(lst))

# 4
data=string1.split(' ')
lst=[len(data) for data in data]
print(lst)

# 5
lst=[i for i in range(1,100) if i%5==0 and i%7==0 ]
print(lst)

# 6
lst=[words[::-1] for words in reversed(words)]
print(lst)

