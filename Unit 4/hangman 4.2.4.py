import calendar

date_input = input("Please enter a date in the format dd/mm/yyyy: ")
day = calendar.weekday(int(date_input[-4::]), int(date_input[3:5]), int(date_input[:2]))
print(calendar.day_name[day])