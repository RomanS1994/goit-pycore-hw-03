from datetime import datetime


def get_days_from_today(date):
    '''
    Calculates the difference between two dates
    
    Parameters:
    date (str).

    Returns:
    result.days(int)
    '''
    try:
        datetime_obj = datetime.strptime(date, "%Y-%m-%d").date()
    
        date_now = datetime.now().date()
        # print(date_now)

        result = date_now - datetime_obj
        # print(result)
        return result.days
    except:
        return "Enter the correct format"


print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2021-10"))
