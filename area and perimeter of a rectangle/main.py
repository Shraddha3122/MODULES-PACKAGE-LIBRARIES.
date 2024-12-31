# Create a Python module with a function that computes the area and perimeter of a rectangle. Import and use it in another script.



from rectangle import rectangle_area, rectangle_perimeter

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    area = rectangle_area(length, width)
    perimeter = rectangle_perimeter(length, width)
    
    print(f"The area of the rectangle is: {area}")
    print(f"The perimeter of the rectangle is: {perimeter}")

if __name__ == "__main__":
    main()

