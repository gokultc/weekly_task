# 153 = 1*1 + 5*5 + 3*3
num=153
temp=num
add=0
s=0
m=len(str(num))
for i in range(1,num+1):
    add=num%10              #15.3   1.5     1
    num=num//10             #15     1       0
    s+=add**m               #3**3   5**3    1**3
if temp==s:
    print("arm")
else:
    print('not')