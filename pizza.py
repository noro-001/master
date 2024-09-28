S_price = 15 
M_price = 20 
L_price = 25 
bill = 0

print("Welcome to Python pizza!")

size_answer = input("Which one you want? S, M or L: ")

if size_answer == "S":
    bill += S_price
    peperoni = input("Do you want to add a peperoni?(Y or N): ")
    if peperoni == "Y":
        bill += 2
elif size_answer == "M":
    bill += M_price
    peperoni = input("Do you want to add a peperoni?(Y or N): ")
    if peperoni == "Y":
        bill += 3
elif size_answer == "L":
    bill += L_price
    peperoni = input("Do you want to add a peperoni?(Y or N): ")
    if peperoni == "Y":
        bill +=3

cheese = input("Do you want extra cheese?(Y or N):")
if cheese == "Y":
    bill += 1 

print(f"Your final bill is {bill}")

