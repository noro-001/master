year_input = eval(input("Enter the year you want to check: "))

if year_input % 4 == 0:
    print(f"{year_input} is a leap year.")
elif year_input % 4 != 0:
    print(f"{year_input} isn't a leap year")