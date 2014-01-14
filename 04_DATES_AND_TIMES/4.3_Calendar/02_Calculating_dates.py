import calendar
import pprint
pprint.pprint(calendar.monthcalendar(2011, 7))

print '==========================================='
for month in range(1,13):
	c = calendar.monthcalendar(2011, month)
	first_week = c[0]
	second_week = c[1]
	third_week = c[2]

	if first_week[calendar.THURSDAY]:
		meeting_date = second_week[calendar.THURSDAY]
	else:
		meeting_date = third_week[calendar.THURSDAY]
	print '%3s:%2s' % (calendar.month_abbr[month],meeting_date)