print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size == 'S':
    bill=15
    print(f"your small pizza prize will be {bill}$")
    if pepperoni == 'Y':
        bill+=2
        print(f"after adding pepperoni to your small pizza prize will be {bill}$")
    else:
        print(f"your small pizza prize will be {bill}$")
    if extra_cheese == 'Y':
        bill+=1
        print(f"your small pizza prize will be {bill}$")
    else:
        print(f"your small pizza prize will be {bill}$")
elif size =='M':
    bill=20
    if pepperoni == 'Y':
        bill+=3
        print(f"your medium pizza prize will be {bill}$")
    else:
        print(f"your medium pizza prize will be {bill}$")
    if extra_cheese == 'Y':
        bill+=1
        print(f"your medium pizza prize will be {bill}$")
    else:
        print(f"your medium pizza prize will be {bill}$")
elif size== 'L':
    bill=25
    if pepperoni == 'Y':
        bill+=3
        print(f"your large pizza prize will be {bill}$")
    else:
        print(f"your large pizza prize will be {bill}$")
    if extra_cheese == 'Y':
        bill+=1
        print(f"your large pizza prize will be {bill}$")
    else:
        print(f"your large pizza prize will be {bill}$")
else:
    print("Please enter a valid size")