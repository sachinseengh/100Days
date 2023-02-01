def days_in_month(year,month):
    month_days=[31,28,31,30,31,31,31,30,30,30,31,31]
    if((year%400==0) or (year%4==0 and year%100!=0)):
        days=month_days[month-1] +1
        return days
    else:
        days=month_days[month-1]
        return days




print(days_in_month(2008,2))
list_of_leap_year=[2000,2002,2004,2008,2012]
# year=int(input("Enter the year\n"))

# if((year%400==0) or (year%4==0 and  year%100 !=0)):
#     print("leap")
# else:
#     print("not leap")