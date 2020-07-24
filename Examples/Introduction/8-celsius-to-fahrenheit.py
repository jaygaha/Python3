# Formula celsius * 1.8 = fahrenheit - 32
# Python program to convert temperature in celsius to fahrenheit
print("Celsius to Fahrenheit")
celsius = float(input("Enter a value in celsius: "))

# Calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print("%0.1f degree celcius is equal to %0.1f degree fahrenheit" %(celsius, fahrenheit))

print("\n\nFahrenheit to Celsius")

fahrenheit1 = float(input("Enter a fahrenheit: "))

# Calculate celsius
celsius1 = (fahrenheit1 - 32) / 1.8
print("%0.1f degree fahrenheit is equal to %0.1f degree celsius" %(fahrenheit1, celsius1))