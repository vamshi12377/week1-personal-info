# Personal Information Manager
# Week 1 Python Project

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
name = "Alex Johnson"       # Your name (string)
age = 22                    # Your age (integer)
city = "San Francisco"      # Your city (string)
hobby = "playing guitar"    # Your hobby (string)

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

# Validate favorite food input
favorite_food = input("What's your favorite food? ")
while favorite_food.strip() == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ")

# Validate favorite color input
favorite_color = input("What's your favorite color? ")
while favorite_color.strip() == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

# Calculate age in months
age_in_months = age * 12

# Display all information using f-strings
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name:          {name}")
print(f"Age:           {age} years ({age_in_months} months old)")
print(f"City:          {city}")
print(f"Hobby:         {hobby}")
print()
print(f"Favorite Food:  {favorite_food.capitalize()}")
print(f"Favorite Color: {favorite_color.capitalize()}")
print()

# Goodbye message
print("=" * 40)
print("   Thanks for using this program!")
print("=" * 40)
