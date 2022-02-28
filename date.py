from datetime import datetime
from datetime import timedelta
import re

result = (datetime.now())
simdi = datetime.now()

result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second
result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y ')
result = datetime.strftime(simdi,'%X')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %A')

# t = '21 Nisan 2019'

# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

t = '21 April 2019 hour 10:12:30'

result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,21,12,10,30)     

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) #saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)
# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730,minutes=20)

result = simdi - timedelta(days=10)

print(result)
