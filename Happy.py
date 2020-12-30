import datetime
# today
now = datetime.datetime.now()

is_today = now.day == 25
is_today_january = now.month == 1
is_remains = datetime.datetime(2021, 1, 25)

if is_today and is_today_january:
    print('Hooray, birthday')
else:
    remains = is_remains - now
    print(remains.days)











