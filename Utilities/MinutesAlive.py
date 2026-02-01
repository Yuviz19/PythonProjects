"""
Challange - Minutes Alive Calculator

Write a python Script that calculates approximately how many minutes old a person is,
based on their age in years.

Your Program should:-
1. Ask the user for their age in years.(accept float values too.)
2. Convert the age into:
    - Total Days
    - Total Hours
    - Total Minutes
3. Display the result in a readable format.

Assumptions:
- You can account 365.25 days/year for a leap year
- You don't need to handle time zones or exact birthdates in this version

Bonus:
- Add comma formating for large numbers
- Let the user try again without restarting the Program
"""

DAYS_IN_YEARS = 365.25
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

def total_days(age):
    global DAYS_IN_YEARS
    return age * DAYS_IN_YEARS

def total_hours(age):
    global HOURS_IN_DAY
    return HOURS_IN_DAY * total_days(age)

def total_minutes(age):
    global MINUTES_IN_HOUR
    return MINUTES_IN_HOUR * total_hours(age)

def main():
    while True:
        try:
            print(f"{"*" * 5} HOW OLD YOU ACTUALLY ARE {"*" * 5}\n")    
            age = float(input("Enter Your Age: "))
            days = total_days(age)
            hours = total_hours(age)
            minutes = total_minutes(age)

            print(f"{"*" * 30}\n")
            print(f"You Are {age:,.2f} Years Old")
            print(f"You Are {days:,.2f} Days Old")
            print(f"You are {hours:,.2f} Hours Old")
            print(f"You are {minutes:,.2f} Minutes Old\n")
            print(f"{"*" * 30}\n")

        except ValueError:
            print("Invalid Input. Please Try again Later.")
            break

if __name__ == "__main__":
    main()


