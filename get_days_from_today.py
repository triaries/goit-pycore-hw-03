from datetime import datetime

def get_days_from_today(date):
    
    date_format = '%Y-%m-%d'
    
    try:
        #Convert date from str -> datetime, leave only the date
        d = datetime.strptime(date, date_format).date()

    except:
        print('Invalid date format')
        return None
    
    #Get today's date
    td = datetime.today().date()

    #Get the date difference in days
    res = (td - d).days
    
    return res
