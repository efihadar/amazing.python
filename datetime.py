import datetime
import calendar

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y')
    day = born.weekday()
    return (calendar.day_name[day])

#day month year
date = '25 08 1985'
print(findDay(date))
