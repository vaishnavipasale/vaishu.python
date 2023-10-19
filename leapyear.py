Check if a year is a leap year
year = int (input("Enter a year"))
if (year%4==0) and (year%100==0):
    print(f"{year} is leap year")
if (year%4==0) and (year%100!=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
