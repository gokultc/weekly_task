# print the name if the weight over 4500 in uppercase

dic={'car': 3500,'bus':8000,'minibus':5000,'bike':500,'cycle':50}
lst=[i.upper() for i in dic if dic[i]>4500]
print(lst)

