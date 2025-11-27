#Input values
Nanometer = float(input("Enter the value in Nanometer: "))
Micrometer = float(input("Enter the value in Micrometer: "))
Millimeter = float(input("Enter the value in Millimeter: "))
Centimeter = float(input("Enter the value in Centimeter: "))
Decimeter = float(input("Enter the value in Decimeter: "))
Kilometer = float(input("Enter the value in Kilometer: "))

#Calculation
Meter1 = Nanometer * (10**9)
Meter2 = Micrometer * (10**6)
Meter3 = Millimeter * (10**3)
Meter4 = Centimeter * (10**2)
Meter5 = Decimeter * (10**1)
Meter6 = Kilometer * (10**3)

#printing of values
print(f"{Nanometer} Nanometer = {Meter1} Meter")
print(f"{Micrometer} Micrometer = {Meter2} Meter")
print(f"{Millimeter} Millimeter = {Meter3} Meter")
print(f"{Centimeter} Centimeter = {Meter4} Meter")
print(f"{Decimeter} Decimeter = {Meter5} Meter")
print(f"{Kilometer} Kilometer = {Meter6} Meter")


