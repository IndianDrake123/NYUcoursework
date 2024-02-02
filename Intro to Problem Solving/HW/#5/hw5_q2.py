"""
Author: Brian Thomas 
Assignment / Part: HW5 - Q2 Le Grand Jour
Date due: October 26, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def get_decimal_time(hours, minutes, seconds):
    hours, minutes, seconds = float(hours), float(minutes), float(seconds)
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    decimal_hours = (total_seconds)//10000
    decimal_minutes = (total_seconds % 10000)//100
    decimal_seconds = total_seconds % 100
    decimal_time = f"{int(decimal_hours)}:{int(decimal_minutes)}:{int(decimal_seconds)}"

    return decimal_time

def get_decimal_date(month, day, year):
    month = float(month)
    day = float(day)
    year = float(year)
    if month < 13 and month > 1:
        if month == 1:
            french_month = "Nivôse"
        elif month == 2:
            french_month = "Pluviôse"
        elif month == 3:
            french_month = "Ventôse"
        elif month == 4:
            french_month = "Germinal"
        elif month == 5:
            french_month = "Floréal"
        elif month == 6:
            french_month = "Prairial"
        elif month == 7:
            french_month = "Messidor"
        elif month == 8:
            french_month = "Thermidor"
        elif month == 9:
            french_month = "Fructidor"
        elif month == 10:
            french_month = "Vendémiaire"
        elif month == 11:
            french_month = "Brumaire"
        elif month == 12:
            french_month = "Frimaire"

        decade = ((day - 1)//10) + 1
        year -= 1792
        result = f"{int(day)} {french_month} Year {int(year)}, Décade {int(decade)}"
    else:
        result = 'invalid month was given'

    if day > 32:
        result = 'invalid day was given'

    return result

def get_french_datetime(gregorian_datetime):
    gregorian_datetime.rstrip()
    hour_pos = gregorian_datetime.find(':')
    min_pos = gregorian_datetime.find(':', hour_pos + 1)
    hours = gregorian_datetime[0:hour_pos]
    min = gregorian_datetime[hour_pos + 1:min_pos]
    sec = gregorian_datetime[min_pos + 1:gregorian_datetime.find(' ')]
    time = get_decimal_time(hours, min, sec)

    month_pos = gregorian_datetime.find('/') 
    day_pos = gregorian_datetime.find('/', month_pos + 1) 
    month = gregorian_datetime[gregorian_datetime.find(' '):month_pos]
    day = gregorian_datetime[month_pos + 1:day_pos]
    year = gregorian_datetime[day_pos + 1:]
    date = ' ' + get_decimal_date(month, day, year)

    return time + date

