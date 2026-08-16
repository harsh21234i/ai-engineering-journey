#TIP CALCULATOR PROJECT
print("Welcome to the tip calculator!")
bill=float(input("Enter your bill: "))
tip=float(input("Enter your tip percent: "))
people=int(input("Enter your people: "))
total_bill_each=float((bill+tip)/people)
per_person=str(input("Enter your per_person: " + str(total_bill_each)))




