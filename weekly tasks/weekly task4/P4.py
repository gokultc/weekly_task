#       1
#      121
#     12321

for i in range(1,5):
    for j in range(5,i,-1): #5
        print(' ',end='')
    for k in range(1,i+1):  #
        print(k,end='')
    for l in range(i-1,0,-1):
        print(l,end='')
    print()