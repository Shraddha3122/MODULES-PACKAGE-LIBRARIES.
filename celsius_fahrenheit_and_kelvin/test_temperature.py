# Write a module to convert temperatures between Celsius, 
#Fahrenheit, and Kelvin. Test it in a separate script.

# test_temperature.py

from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit
)

def test_temperature_conversions():
    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100

    # Test Celsius to Kelvin
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(100) == 373.15

    # Test Kelvin to Celsius
    assert kelvin_to_celsius(273.15) == 0
    assert kelvin_to_celsius(373.15) == 100

    # Test Fahrenheit to Kelvin
    assert fahrenheit_to_kelvin(32) == 273.15
    assert fahrenheit_to_kelvin(212) == 373.15

    # Test Kelvin to Fahrenheit
    assert kelvin_to_fahrenheit(273.15) == 32
    assert kelvin_to_fahrenheit(373.15) == 212

    print("All tests passed!")

if __name__ == "__main__":
    test_temperature_conversions()