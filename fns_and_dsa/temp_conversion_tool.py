FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter the temperature to convert: ")
    c_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if c_f == "C":
        print(f"{temp_input}°F is {convert_to_fahrenheit(temp_input)}°C")
    else:
        print(f"{temp_input}°C is {convert_to_celsius(temp_input)}°F")
