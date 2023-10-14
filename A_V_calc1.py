'''
# A_V_calc.py

TPRG 2131 Fall 2023 Assignment 1
October,11 2023
KHARI WALLACE, 100807131,
Khari Wallace <khari.wallace@dcmail.ca>




*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********
'''


# A/V calculator

# Define the calculation functions

# Function to calculate volume for calculation 1 (Sphere volume)
def calculate_volume_1(dimensions):
    if len(dimensions) >= 1:
        radius = dimensions[0]
        volume = (4/3) * 3.14159265358979323846 * (radius ** 3)
        return volume
    return none

# Function to calculate volume for calculation 2 (Cube volume)
def calculate_volume_2(dimensions):
    if len(dimensions) >= 1:
        side_length = dimensions[0]
        volume = side_length ** 3
        return volume
    return none

# Function to calculate area for calculation 3 (Rectangle area)
def calculate_area_1(dimensions):
    if len(dimensions) >= 2:
        length, width = dimensions
        area = length * width
        return area
    return none

# Function to calculate area for calculation 4 (Triangle area)
def calculate_area_2(dimensions):
    if len(dimensions) >= 2:
        base, height = dimensions
        area = (1/2) * base * height
        return area
    return none

# Function to calculate area for calculation 5 (Trapezoid area)
def calculate_area_3(dimensions):
    if len(dimensions) >= 3:
        base1, base2, height = dimensions
        area = (1/2) * (base1 + base2) * height
        return area
    return none

# Function to get user input for dimensions
def get_dimensions(calculation_choice):
    dimensions = []
    
    if calculation_choice == 1:
        # Prompt for dimensions needed for calculation 1 (Sphere volume)
        radius = float(input("Enter the radius: "))
        dimensions.append(radius)
    
    elif calculation_choice == 2:
        # Prompt for dimensions needed for calculation 2 (Cube Volume)
        side_length = float(input("Enter the side length: "))
        dimensions.append(side_length)
    
    elif calculation_choice == 3:
        # Prompt for dimensions needed for calculation 3 (Rectangle area)
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        dimensions.extend([length, width])
    
    elif calculation_choice == 4:
        # Prompt for dimensions needed for calculation 4 (Triangle area)
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        dimensions.extend([base, height])
    
    elif calculation_choice == 5:
        # Prompt for dimensions needed for calculation 5 (Trapezoid area)
        base1 = float(input("Enter base1: "))
        base2 = float(input("Enter base2: "))
        height = float(input("Enter the height: "))
        dimensions.extend([base1, base2, height])

    return dimensions

# Function to view equations and results
def view_equations(calculation, dimensions, result):
    # Define equations for each calculation
    equations = {
       1: f"Sphere Volume: V = (4/3) * π * r^3, where r = {dimensions[0] if len(dimensions) >= 1 else 'N/A'}",
        2: f"Cube Volume: V = side_length^3, where side_length = {dimensions[0] if len(dimensions) >= 1 else 'N/A'}",
        3: f"Rectangle Area: A = length * width, where length = {dimensions[0] if len(dimensions) >= 1 else 'N/A'}, width = {dimensions[1] if len(dimensions) >= 2 else 'N/A'}",
        4: f"Triangle Area: A = (1/2) * base * height, where base = {dimensions[0] if len(dimensions) >= 1 else 'N/A'}, height = {dimensions[1] if len(dimensions) >= 2 else 'N/A'}",
        5: f"Trapezoid Area: A = (1/2) * (base1 + base2) * height, where base1 = {dimensions[0] if len(dimensions) >= 1 else 'N/A'}, base2 = {dimensions[1] if len(dimensions) >= 2 else 'N/A'}, height = {dimensions[2] if len(dimensions) >= 3 else 'N/A'}"
    }
    
    if calculation in equations:
        # Display the equation and result for the selected calculation
        print(f"Equation for Calculation {calculation}:")
        print(equations[calculation])
    else:
        print("Invalid calculation choice")

    if result is not None:
        print(f"Result: {result}\n")
    else:
        print("Insufficient dimensions for calculation. Please provide the required number of dimensions.\n")


# Function to view in default mode (showing only the result)
def view_default(result):
    # Display only the result
    print(f"Result: {result}\n")

# Main program loop
if __name__ == "__main__":
    while True:
        print("A/V calculator Menu")
        print("(Level 0)")
        print("Enter Q/q to quit")
        print("Enter V/v to change the calculated view")
        
        # Add options for level 1 menu here
        
        choice = input("Enter your choice: ").lower()
        
        if choice == 'q':
            break
        elif choice == 'v':
            # Change view mode
            pass
        elif choice.isdigit() and 1 <= int(choice) <= 5:
            calculation_choice = int(choice)
            dimensions = get_dimensions(calculation_choice)
            
            # Perform the selected calculation based on calculation_choice
            if calculation_choice == 1:
                result = calculate_volume_1(dimensions)
            elif calculation_choice == 2:
                result = calculate_volume_2(dimensions)
            elif calculation_choice == 3:
                result = calculate_area_1(dimensions)
            elif calculation_choice == 4:
                result = calculate_area_2(dimensions)
            elif calculation_choice == 5:
                result = calculate_area_3(dimensions)
            
            view_equations(calculation_choice, dimensions, result)
        else:
            print("Invalid choice. Please try again.")


