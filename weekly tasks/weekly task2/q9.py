def monument(x):
    if city.lower()=='delhi':
        print("Monumnet in ",city," is Red Fort")
    elif city.lower()=='agra':
        print("Monumnet in ",city,"is Taj Mahal")
    elif city.lower()=='jaipur':
        print("Monumnet in ",city,"is Jal Mahal")

city=input("Enter the city name :")

monument(city)

