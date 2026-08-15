import datetime
import calendar

def parse_dob(input_str):
    """Parse DOB in formats: YYYY-MM-DD or DD-MM-YYYY or DD/MM/YYYY"""
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.datetime.strptime(input_str, fmt).date()
        except ValueError:
            continue
    raise ValueError("Date format not recognized. Use YYYY-MM-DD or DD-MM-YYYY or DD/MM/YYYY.")

def age_years_months_days(birth_date, on_date=None):
    """Return (years, months, days) difference between birth_date and on_date (defaults to today)."""
    if on_date is None:
        on_date = datetime.date.today()
    if birth_date > on_date:
        raise ValueError("Birth date is in the future.")
    
    # Start with basic year difference and then adjust months/days
    years = on_date.year - birth_date.year
    months = on_date.month - birth_date.month
    days = on_date.day - birth_date.day

    if days < 0:
        # borrow days from previous month
        prev_month = on_date.month - 1 or 12
        prev_month_year = on_date.year if on_date.month != 1 else on_date.year - 1
        days_in_prev_month = calendar.monthrange(prev_month_year, prev_month)[1]
        days += days_in_prev_month
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return years, months, days

def birthday_weekday(birth_date):
    """Return weekday name for the birth date using calendar module."""
    weekday_index = calendar.weekday(birth_date.year, birth_date.month, birth_date.day)
    return calendar.day_name[weekday_index]

def is_birth_year_leap(birth_date):
    return calendar.isleap(birth_date.year)

def interactive_age_calculator():
    s = input("Enter your date of birth (DD-MM-YYYY or YYYY-MM-DD): ").strip()
    bd = parse_dob(s)
    y, m, d = age_years_months_days(bd)
    print(f"\nYou were born on {bd.isoformat()} ({birthday_weekday(bd)}).")
    print(f"Birth year {bd.year} is a leap year: {is_birth_year_leap(bd)}.")
    print(f"Your age is: {y} years, {m} months, and {d} days.")
