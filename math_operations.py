# Function to perform basic mathematical operations

def perform_operations(num1, num2):

    addition = num1 + num2

    subtraction = num1 - num2

    multiplication = num1 * num2

    division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

   

    return addition, subtraction, multiplication, division

 

# Predefined numbers

num1 = 10

num2 = 5

 

# Perform operations

addition, subtraction, multiplication, division = perform_operations(num1, num2)

 

# Display the results

print(f"Addition: {num1} + {num2} = {addition}")

print(f"Subtraction: {num1} - {num2} = {subtraction}")

print(f"Multiplication: {num1} * {num2} = {multiplication}")

print(f"Division: {num1} / {num2} = {division}")