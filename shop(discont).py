product1=int(input("enter the number"))
product2=int(input("enter the number"))
product3=int(input("enter the number"))
product4=int(input("enter the number"))
product5=int(input("enter the number"))
product6=int(input("enter the number"))
product7=int(input("enter the number"))
product8=int(input("enter the number"))
product9=int(input("enter the number"))
product10=int(input("enter the number"))

total=(product1+product2+product3+product4+product5+product6+product7+product8+product9+product10)
if total > 2000:
    discount = total * 0.20
    total_after_discount = total - discount
    print("Total amount before discount:",total)
    print("Discount applied:",discount)
    print("Total amount after 20% discount:",total_after_discount)
else:
    print("Total amount:",total)
    print("No discount applied as total is less than or equal to 2000.")
