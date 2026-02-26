from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.02.28"},
    {"name": "Jane Smith", "birthday": "1990.02.24"},
    {"name": "Leap Year Baby", "birthday": "2000.02.29"} # Тестовий випадок
]

def get_upcoming_birthdays(users):

    today = datetime.today().date()
    print(today)
    users_with_upcoming_birthdays = []
    for user in users:
        # Parse string birthday to date object
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Set birthday to the current year (handle leap year case)
        try:
            next_birthday = user_birthday.replace(year=today.year)
        except ValueError:
            next_birthday = user_birthday.replace(year=today.year, month=3, day=1)

        # If birthday has already passed this year, move to next year
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        # Check if the birthday is within the next 7 days
        if 0 <= (next_birthday - today).days <= 7:
            day_of_week = next_birthday.isoweekday()

            # If weekend, shift congratulation date to Monday
            if day_of_week == 6:
                next_birthday += timedelta(days=2)
            elif day_of_week == 7:
                next_birthday += timedelta(days=1)

            # Prepare and collect user data
            user_data = {'name': user["name"], 'congratulation_date': next_birthday.strftime("%Y.%m.%d")}
            users_with_upcoming_birthdays.append(user_data)
        
        
    
    return users_with_upcoming_birthdays


print(get_upcoming_birthdays(users))




