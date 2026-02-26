import random

def get_numbers_ticket(min, max, quantity):
     #Input data validation
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        print('Use integer numbers')
        return []
    if min < 1 or max > 1000:
        print('Invalid input data')
        return []
    if not (0 < quantity <= max - min + 1):
        print('Invalid input data')
        return []
    
    #Set for unique random numbers
    a = set()
    while len(a) < quantity:
        #Get random int from min to max 
        rand = random.randint(min, max)
        #Add random int to set
        a.add(rand)
    
    return sorted(a)
    
