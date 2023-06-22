# Please enter your gender (M or F): F
# Enter your birthdate (YYYY-MM-DD): 2001-03-21
# Enter your weight in U.S. pounds: 125
# Enter your height in U.S. inches: 54
# Age (years): 19
# Weight (kg): 56.70
# Height (cm): 137.2
# Body mass index: 30.1
# Basal metabolic rate (kcal/day): 1315

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD):")
    height = float(input("Enter your height in U.S. inches:"))
    weight = float(input("Enter your weight in U.S. pounds:"))

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    age = compute_age(birthdate)
    cm = cm_from_in(height)
    kg = kg_from_lb(weight)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, age)

    # Print the results for the user to see.

    print(f"Age (years):{age}")
    print(f"Weight (kg):{kg:.2f}")
    print(f"Height (cm):{cm:.2f}")
    print(f"Body mass index:{bmi:.2f}")
    print(f"Basal metabolic rate (kcal/day):{bmr:.2f}")
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kilograms = pounds * 0.45359237

    return kilograms


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    centimeters = inches * 2.54

    return centimeters


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight)/(height**2)

    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "M" or gender == "m":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    elif gender == "F" or gender == "f":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age

    return bmr


# Call the main function so that
# this program will start executing.

main()