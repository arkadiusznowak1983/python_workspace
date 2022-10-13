from datetime import datetime, date, timedelta
import time
import calendar


def date_and_time_operations():
    # Result:
    # gmt => time.struct_time(tm_year=2022, tm_mon=10, tm_mday=13, tm_hour=6, tm_min=20, tm_sec=59, tm_wday=3, tm_yday=286, tm_isdst=0) 0 Thu Oct 13 06:20:59 2022
    # local => time.struct_time(tm_year=2022, tm_mon=10, tm_mday=13, tm_hour=8, tm_min=20, tm_sec=59, tm_wday=3, tm_yday=286, tm_isdst=1) 1 Thu Oct 13 08:20:59 2022
    # default local => Thu Oct 13 08:20:59 2022
    # yday => 286
    # today => 2022-10-13 08:20:59.801794
    # now =>  2022-10-13 08:20:59.801793
    # utcnow =>  2022-10-13 06:20:59.801793
    # timestamp =>  1665642059.801793
    # strftime =>  2022-10-13
    # strptime => 1983-10-25 07:00:02
    # time from my birth => 14233 days, 8:20:59.811828
    # seconds from 14233 days ago => 1229731200.0
    # today + delta => 2022-11-01 12:20:59.811828
    #
    timestamp = time.time()
    gm = time.gmtime(timestamp)
    lt = time.localtime(timestamp)
    print('gmt =>', gm, gm.tm_isdst, time.asctime(gm))
    print('local =>', lt, lt.tm_isdst, time.asctime(lt))
    print('default local =>', time.asctime())
    print('yday =>', lt.tm_yday)

    print('today =>', datetime.today())
    print('now => ', datetime.now())
    print('utcnow => ', datetime.utcnow())
    print('timestamp => ', datetime.now().timestamp())
    print('strftime => ', date.today().strftime('%Y-%m-%d'))

    print('strptime =>', datetime.strptime("1983-10-25 07:00:02", "%Y-%m-%d %H:%M:%S"))

    print('time from my birth =>', datetime.today() - datetime.strptime("1983-10-25", "%Y-%m-%d"))
    print('seconds from 14233 days ago =>', timedelta(days=14233).total_seconds())
    print('today + delta =>', datetime.today() + timedelta(weeks=2, days=3, hours=4)+timedelta(days=2))


def calendar_operations():
    c = calendar.Calendar()
    # for date in c.itermonthdates(2022, 10):
    #     print(date, calendar.day_name[date.weekday()], sep=" ")
    # for date in c.itermonthdays4(2022, 10):
    #     print(date,  sep=" ")
    for data in c.monthdays2calendar(2020, 12):
        print(data)



calendar_operations()