from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    '''
    Function that generates a birthday reminder for this week

    Parameters:
    users (list) - object with dates of birthdays
    Returns:
    list(str) - with phone numbers 
    '''
    today = datetime.today().date()
    print(f"today is: {today}")


    reminder = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = date(today.year, birthday.month, birthday.day)
        # print(birthday_this_year)
        if birthday_this_year < today:
            birthday_this_year = date(today.year + 1, birthday.month, birthday.day)
       
       
        days_until_birthday = (birthday_this_year - today).days

        if days_until_birthday <= 7:
            if(birthday_this_year.weekday() == 5):
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif(birthday_this_year.weekday() == 6):
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year

            congratulation_date_str = datetime.strftime(congratulation_date, '%Y.%m.%d')
            reminder.append({'name': user['name'],
                        'congratulation_date': congratulation_date_str}) 

    return reminder

users = [
    {"name": "John Doe", "birthday": "1985.10.06"},
    {"name": "Jane Smith", "birthday": "1990.10.07"},
    {"name": "Nick Smith", "birthday": "1990.10.11"},
    
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)




