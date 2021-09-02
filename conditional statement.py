print("Enter your age")
age = int(input(""))
if age<1:
    print("invalid input")
elif age<6:
    print("Little Baby ticket is Free")
elif 6<=age<=17:
    print("You got child discount on your ticket is 15%")
elif 18<=age<=26:
    print("You got student discount on your ticket is 10%")
elif 27<=age<=66:
    print("You have to pay full price of your ticket")
else:
    print("You got senior citizen discount on your ticket is 15%")

