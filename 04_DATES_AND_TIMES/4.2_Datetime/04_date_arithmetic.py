import datetime
today = datetime.date.today()
print 'today:',today
one_day = datetime.timedelta(days=1)
print 'One day :',one_day
yesterday = today - one_day
print 'yesterday :',yesterday
tomorrow = today+one_day
print 'Tomorrow :',tomorrow
print 
print 'tomorrow-yesterday:',tomorrow-yesterday
print 'yesterday-tomorrow:',yesterday-tomorrow