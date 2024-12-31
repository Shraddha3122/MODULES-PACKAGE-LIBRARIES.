# Write a program using the math module to compute the sine, cosine, and tangent of a given angle.



import math

def compute_trig_functions(angle_degrees):
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Compute sine, cosine, and tangent
    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)
    
    return sine_value, cosine_value, tangent_value

def main():
    # Get user input
    angle_degrees = float(input("Enter the angle in degrees: "))
    
    # Compute the trigonometric functions
    sine, cosine, tangent = compute_trig_functions(angle_degrees)
    
    # Display the results
    print(f"Sine of {angle_degrees} degrees: {sine}")
    print(f"Cosine of {angle_degrees} degrees: {cosine}")
    print(f"Tangent of {angle_degrees} degrees: {tangent}")

if __name__ == "__main__":
    main()