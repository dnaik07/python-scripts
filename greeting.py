# Function to create a personalized greeting

def create_greeting(first_name, last_name):

    full_name = first_name + " " + last_name

    greeting = f"Hello, {full_name}! Welcome!"

    return greeting

 

# Predefined first name and last name

first_name = "John"

last_name = "Doe"

 

# Create and print the personalized greeting

greeting_message = create_greeting(first_name, last_name)

print(greeting_message)