

n=int(input("enter the length of the identifier :"))
chars=[]
print("enter the chararacters :")
for i in range(n):
    chars.append(input(f"character{i+1}"))

ind=[0]*n
total=len(chars)**n
for i in range(total):
    word=''.join(chars[i] for i in ind)
    print(word)


