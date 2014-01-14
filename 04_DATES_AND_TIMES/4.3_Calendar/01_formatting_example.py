import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2011, 7)
print '==========================================='
import pprint
cal = calendar.Calendar(calendar.SUNDAY)

cal_data = cal.yeardays2calendar(2011,3)
# print cal_data
print 'len(cal_data)    :',len(cal_data)

top_months = cal_data[0]
print 'len(top_months)  :',len(top_months)

first_month = top_months[0]
print 'len(first_month)  :',len(first_month)

print 'first_month:'
pprint.pprint(first_month)
print '==========================================='
cal1 = calendar.TextCalendar(calendar.SUNDAY)
print cal1.formatyear(2011,2,1,1,3)
