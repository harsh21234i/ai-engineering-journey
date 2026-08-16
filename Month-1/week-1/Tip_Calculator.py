#TIP CALCULATOR PROJECT
print("Welcome to the tip calculator!")
bill=float(input("Enter your bill: "))
tip=int(input("Enter your tip percent: "))
people=int(input("Enter your people: "))
tip_percent=tip/100
total_bill=bill+bill*tip_percent
bill_per_person=round(total_bill/people,2)
per_person=str(input("Enter your per_person: " + str(bill_per_person)))




