print()

feet = float(input("Enter a length in feet: "))
inches = feet * 12
print(f"{feet} feet is {inches} inches.\n")

minutes = float(input("Enter a duration in minutes: "))
seconds = minutes * 60
print(f"{minutes} minutes is {seconds} seconds.\n")

c = float(input("Enter a temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"{c} degrees Celsius is {f} degrees Fahrenheit.")
