f=open('C:/Users/GOKUL/Downloads/movies_cleaned_pandas.csv','r')
for i in f:
    data=i.rstrip('/n').split(',')
    # 1
    rating=data[3]
    if rating>'3':
        print(data[1:4])
    # 2
    year=data[2]
    if year=='2000':
        print(data[1:3])
        print(data[4])
    # 3

    # 4
    if year>'2005' and rating >'4':
        print(data[1:4])

    # 5 - alphabet count

