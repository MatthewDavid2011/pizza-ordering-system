#Pizza ordering system
print("Welcome to the Pizza Shop")
price=0
print("Cheese=£20\nPepperoni=£23\nVeg Delux=£30\nSausage Filled Crust=£32\nGarlic Bread=£15\nDeserts\nBrownie=£10\nEbony Ivory=£12\nNutylious honey comb=£25")
x= input("Which pizza would you like?")
if x == ("Cheese"):
    price= price+20
elif x == ("Pepperoni"):
        price= 23
elif x == ("Veg Delux"):
    price= 30
elif x == ("Sausage Filled Crust"):
    price= 32
elif x == ("Garlic Bread"):
    price= 15
elif x == ("Brownie"):
    price= 10
elif x == ("Ebony Ivory"):
    price= 12
elif x == ("Nutylious honey comb"):
    price= 25
else:
    price= 0
xtra = input("Would you like extra cheese y/n")
if x == ("Pepperoni","Cheese","Veg Delux","Sausage Filled Crust"):

    if xtra == ("y"):
        price = price + 5
    elif xtra == ("n"):
        print("Price is the same")

    
print(price)