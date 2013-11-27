from datetime import datetime, timedelta
from time import strftime
from random import uniform, randint

end_date = datetime.now()
start_date = end_date - timedelta(days=90)


def daterange(start_date, end_date):
    for n in range(0, (end_date - start_date).days, randint(1, 7)):
        yield start_date + timedelta(n)

print "delete from samples;"

for n in range(1, 6):
    for single_date in daterange(start_date, end_date):
        date = strftime("%Y-%m-%d", single_date.timetuple())
        value = uniform(0.1, 100)
        print "insert into samples(metric_id, sample_date, value) values(%s, '%s', %s);" % (n, date, value)

# vim: set et sw=4 ts=4:
