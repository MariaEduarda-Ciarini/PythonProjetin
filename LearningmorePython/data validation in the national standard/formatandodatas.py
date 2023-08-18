from datetime import datetime, timedelta

from datesBR import DateBR

'''
today = datetime.today()
tomorrow = datetime.today() + timedelta(days=1, hours=20)
print(tomorrow - today)
'''

today = DateBR()
print(today.time_register())