print("Kilometers to Miles")
km = float(input("Enter value in kilometers: "))

# Conversion factor
conv_fac = 0.621371

# Calculate miles
miles = km * conv_fac
print("%0.2f kilometers is equal to %0.2f miles" %(km, miles))

print("\n\nMiles to Kilometers")
miles1 = float(input("Enter value in miles: "))

kilometers1 = miles1 / conv_fac

print("%0.2f miles is equal to %0.2f kilometers" %(kilometers1, miles1))