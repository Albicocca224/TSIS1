def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit_input = float(input())
celsius_result = fahrenheit_to_celsius(fahrenheit_input)
print(f"{celsius_result:.2f}")
