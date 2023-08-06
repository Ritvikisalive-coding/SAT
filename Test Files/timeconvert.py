from datetime import datetime

timeIn24HourFormat = '17:30'

dateTime = datetime.strptime(timeIn24HourFormat, '%H:%M')
timeIn12HourFormat = dateTime.strftime('%I:%M %p').lstrip('0')

print(timeIn12HourFormat)