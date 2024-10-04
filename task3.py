import re

def normalize_phone(phone_number):
    '''
    Normalize_phone_number and format_phone_number

    Parameters:
    phone_number(str)
    Returns:
    list(str) - with phone numbers 
    '''

    cut_number =  re.sub(r'[^0-9+]', '', phone_number)

    model = '+38'
    if cut_number.startswith(model):
        return cut_number 
    elif  cut_number.startswith('38'):
        return model + cut_number[2:] 
    else:
        return model + cut_number 



raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)