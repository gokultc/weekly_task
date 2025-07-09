q=int(input("Enter the no of products :"))
product = 0
p = 1
while q > 0:
    print("enter the price of the ", p, " st products :")
    product += int(input())
    q -= 1
    p += 1
if product > 1000:
    dis=product*10/100
    total=product-dis
    print("The total price is",product)
    print("The discount is",dis)
    print("The discounted price is",total)
else:
    print("sorry, Discounts aren't availabele to you ")
