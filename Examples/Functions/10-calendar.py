# Python program to display calendar of the given month and year

# importing calendar module
import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month number: "))

if 1 <= mm <= 12: 
# display the calendar
    print(calendar.month(yy, mm))
else:
    print("Invalid month number, please enter between 1 to 12")