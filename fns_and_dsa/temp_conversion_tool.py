# temp_conversion_tool.py

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_SUBTRACT = 32

def celsius_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_TO_CELSIUS_SUBTRACT

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_SUBTRACT) / CELSIUS_TO_FAHRENHEIT_FACTOR

# Example usage
c = float(input("Enter temp in Celsius: "))
print("Fahrenheit:", celsius_to_fahrenheit(c))

f = float(input("Enter temp in Fahrenheit: "))
print("Celsius:", fahrenheit_to_celsius(f))
