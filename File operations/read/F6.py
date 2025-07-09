f=open("C:/Users/GOKUL/Downloads/customer1.txt",'r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
# 10
    loc=data[-1]
    if loc not in dic:
        dic[loc]=1
    else:
        dic[loc]+=1
for k,v in dic.items():
    print(k,":",v)


# # 9
#
#     prof=data[4]
#     if prof not in dic:
#         dic[prof]=1
#     else:
#         dic[prof]+=1
#
# for k,v in dic.items()
#     print(k,":",v)
#
# # 8
#
#     if prof=='Pilot':
#         print(data[1:4])
#
# # 7
#     prof = data[4]
#     age = data[3]
#     if prof == 'Doctor' and age<'40':
#         print(data[1:4])
#
# # 6
#
# # 1
#     age = data[3]
#     if age>'25':
#         print(data[1:4])
#
# # 2
#     age = data[3]
#     if age<"25" and age>"40":
#         print(data[1:4])
#
#
# # 3
#     loc=data[5]
#     if loc=='india':
#         print(data[1:4])
#
#
