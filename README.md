days
----

Print some days in a list.


## Usage

    $ ./days.py  -h

    usage: Print a list of days over a given number of weeks. [-h] [-y YEAR]
                                                              [-m MONTH] [-d DAY]
                                                              [-w WEEKS]
                                                              [-s [Weekday [Weekday ...]]]
                                                              [-c]

    optional arguments:
      -h, --help            show this help message and exit
      -y YEAR, --year YEAR  Year (default is current year: 2018)
      -m MONTH, --month MONTH
                            Month (default is current month: 1)
      -d DAY, --day DAY     Day (default is current day: 22)
      -w WEEKS, --weeks WEEKS
                            Number of weeks. Default is 14.
      -s [Weekday [Weekday ...]], --dows [Weekday [Weekday ...]]
                            Weekdays we wish to print (e.g. Tue, Thu)
      -c, --chunk           Separate output into chunks based on the number of
                            days specified.

## Examples

The default is to print Tuesdays and Thursdays for 14 weeks, starting on the
current day. e.g. if run on Jan 22, 2018 with the default arguments:

    $ ./days.py
    Tue Jan 23
    Thu Jan 25
    Tue Jan 30
    Thu Feb  1
    Tue Feb  6
    Thu Feb  8
    Tue Feb 13
    Thu Feb 15
    Tue Feb 20
    Thu Feb 22
    Tue Feb 27
    Thu Mar  1
    Tue Mar  6
    Thu Mar  8
    Tue Mar 13
    Thu Mar 15
    Tue Mar 20
    Thu Mar 22
    Tue Mar 27
    Thu Mar 29
    Tue Apr  3
    Thu Apr  5
    Tue Apr 10
    Thu Apr 12
    Tue Apr 17
    Thu Apr 19
    Tue Apr 24
    Thu Apr 26

Here, we print 4 weeks of Wednesdays starting on Jan 15, 2018.

    $ ./days.py -y 2017 -m 1 -d 15 -w 4 -s Tue Thu
    Tue Jan 17
    Thu Jan 19
    Tue Jan 24
    Thu Jan 26
    Tue Jan 31
    Thu Feb  2
    Tue Feb  7
    Thu Feb  9

Print Fri, Sat, Sun for three weeks, but also group the output in chunks (`-c`).

    $ ./days.py -s Fri Sat Sun -w 3 -c
    Fri Jan 26
    Sat Jan 27
    Sun Jan 28
    ----------
    Fri Feb  2
    Sat Feb  3
    Sun Feb  4
    ----------
    Fri Feb  9
    Sat Feb 10
    Sun Feb 11
    ----------

## Why?

I sometimes teach a class and find it hand to have a list of dates. I also
haphazardly put this together over several months without ever thinking about
looking at any other tools `¯\_(ツ)_/¯`.
