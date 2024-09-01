months_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_months(year, month):
    if 1 <= month > 12 :
        return "invalid month"
    if month == 2 and is_leap_year(year):
        return 29
    return months_days[month]
print(is_leap_year(int(input("Enter the year:"))))
print(days_in_months(2020, 3))
