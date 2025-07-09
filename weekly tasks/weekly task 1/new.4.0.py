

n=int(input("enter the length of the identifier :"))
chars=[]
print("enter the chararacters :")
for i in range(n):
    chars.append(input(f"character{i+1}"))

total=len(chars)**n
index=[0]*n
for i in range(total):
        word="".join(chars[i]for i in index)
        print(word)

pos=n-1

while pos<=n:
    index[pos]=+1
    if index[pos]<=n:
        print("hello")
        break






