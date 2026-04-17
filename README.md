# Personal Information Manager 🧑‍💻

## Project Description
This is my Week 1 Python project! It's a command-line program that stores and displays personal information using variables, user input, and string formatting.

---

## What I Learned
- **Variables** – How to store different types of data (strings, integers)
- **Input/Output** – Getting user input and displaying results with `print()`
- **String Formatting** – Using f-strings to create clean, readable output
- **Error Handling** – Basic input validation using `while` loops
- **String Methods** – Using `.strip()` and `.capitalize()` to clean input

---

## How to Run This Program

1. Make sure you have **Python 3** installed
2. Open your terminal or command prompt
3. Navigate to the project folder:
   ```
   cd week1-personal-info
   ```
4. Run the program:
   ```
   python personal_info.py
   ```
5. Follow the prompts to enter your information

---

## Features
- Stores static personal info (name, age, city, hobby)
- Gets dynamic input from the user (favorite food and color)
- Validates that inputs are not empty
- Displays all information in a neatly formatted layout
- Calculates and displays age in months

---

## Sample Output

```
========================================
    PERSONAL INFORMATION MANAGER
========================================

Please tell me about yourself:
------------------------------
What's your favorite food? Pizza
What's your favorite color? Blue

========================================
        YOUR INFORMATION
========================================

Name:          Alex Johnson
Age:           22 years (264 months old)
City:          San Francisco
Hobby:         playing guitar

Favorite Food:  Pizza
Favorite Color: Blue

========================================
   Thanks for using this program!
========================================
```

---

## Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| User entering empty input | Used a `while` loop to re-prompt until valid input is given |
| Formatting output neatly | Used f-strings with consistent spacing |
| Cleaning user input | Used `.strip()` to remove extra spaces and `.capitalize()` for proper casing |

---

## Project Structure

```
week1-personal-info/
│── personal_info.py   # Main program
│── README.md          # Project documentation
│── test_inputs.txt    # Sample test inputs
└── .gitignore         # Files to ignore in Git
```
