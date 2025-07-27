# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    # Get temperature input from user
    temp_input = input("Enter the temperature to convert: ").strip()
    temp_value = float(temp_input)  # Attempt to convert to float

    # Get the unit input from user
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Perform conversion
    if unit == 'F':
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted}°C")
    elif unit == 'C':
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
