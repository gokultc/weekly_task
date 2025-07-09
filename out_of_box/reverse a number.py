
num=1234
add=0
rev=0
l=len(str(num))
for i in range(l):
    add=num%10
    num=num//10
    rev=rev*10+add
print(rev)
