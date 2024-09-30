import random

def get_numbers_ticket(min, max, quantity):
    '''
    Generating a random number

    Parameters:
    min (int) - minimum value, 
    max (int) - maximum value, 
    quantity (int) - >= min and <= max.

    Returns:
    List of random numbers.
    '''

    if min < 1 or max > 1000:
        return "Please enter min >= 1 and max <= 1000."
    
    elif quantity < min or quantity > max:
        return "Please Enter quantity between min and max."
    
    else:
        lst = []
        while len(lst) < quantity:
            number = random.randint(min, max)
            if number not in lst:
                lst.append(number)
        
        lst.sort()
        return lst

print(get_numbers_ticket(1, 44, 4))
