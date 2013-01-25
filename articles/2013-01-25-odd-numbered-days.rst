Odd-numbered Days
=================

:category: programming
:tags: python

Whilst chatting on the `#minecraft channel on freenode <irc://chat.freenode.net/minecraft>`_, 
somebody comes out with::

    <Dinnerbone> I love that 50% of thursdays are odd-numbered days
    <Dinnerbone> Makes the near-end-of-week that much more interesting

Which got me thinking...  Are 50% of Thursdays on odd-numbered days?  Probably not, at least not in 
every year.  Some hacky Python code ensues...

.. code-block:: python

    #!/usr/bin/env python3
    import sys
    import datetime
    from collections import defaultdict
     
    def generate_year(year):
        delta = datetime.timedelta(days=1)
        date = datetime.date(year, 1, 1)
     
        while date.year == year:
            yield date
            date = date + delta
     
    day_numbers = defaultdict(list)
     
    for date in generate_year(int(sys.argv[1])):
        day_numbers[date.isoweekday()].append(int(date.strftime('%m')))
     
    day_odd_prob = {}
    for day, nums in day_numbers.items():
        odd = 0
        even = 0
        for n in nums:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
        day_odd_prob[day] = odd / (odd + even)
     
    DAYS = ('Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun')
     
    for day in sorted(day_odd_prob.keys()):
        print('{}\t{}'.format(DAYS[day-1], day_odd_prob[day]))

Now if for some bizarre reason you really want to know what proportion of Thursdays (or any other 
day) fall on odd-numbered days in any given year, you can find out::

    $ python3 odd_days.py 2012
    Mon     0.49056603773584906
    Tues    0.5192307692307693
    Wed     0.4807692307692308
    Thurs   0.5192307692307693
    Fri     0.5
    Sat     0.5
    Sun     0.5094339622641509
     
    $ python3 odd_days.py 2013
    Mon     0.5
    Tues    0.49056603773584906
    Wed     0.5192307692307693
    Thurs   0.5
    Fri     0.5192307692307693
    Sat     0.5
    Sun     0.5
