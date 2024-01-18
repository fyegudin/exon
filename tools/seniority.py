from datetime import datetime


def calculate_seniority(given_date):
    # Given date in the format "YYYY-MM-DD"
    # Convert the given date string to a datetime object
    given_date = datetime.strptime(given_date, "%Y-%m-%d")

    # Calculate the difference between the current date and the given date
    current_date = datetime.now()
    seniority = (current_date - given_date).days
    return seniority
