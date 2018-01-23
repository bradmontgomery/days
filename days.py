#!/usr/bin/env python

import argparse
import calendar

from datetime import date, datetime


def get_days(year, month, day, weeks=14, days=None):
    """Print some days of the calendar sequentially.

    - year: starting year, e.g. 2018
    - month: integer month, e.g. 1 for January
    - day: day of the month, e.g. 20
    - weeks: Number of weeks we print; default is 14
    - days: A list of days of the week in which we're interested. These should
      be written as the first 3 chars; default is ['Tue', 'Thu']

    """
    results = []

    if days is None:
        days = ['Tue', 'Thu']

    c = calendar.Calendar()
    start_date = date(year, month, day)

    num_weeks = 0
    for m in range(13)[month:]:
        for week in c.monthdatescalendar(year, m):
            if num_weeks == weeks:
                return results

            found = False
            for day in week:
                if day < start_date:
                    continue
                dt = day.strftime('%c')
                for dow in days:
                    if dt.startswith(dow) and dt not in results:
                        results.append(dt)
                        found = True
            if found:
                num_weeks += 1
    return results


def main(args):
    results = get_days(args.year, args.month, args.day, args.weeks, args.dows)
    for day in results:
        print(day[:10])


if __name__ == "__main__":

    now = datetime.now()

    parser = argparse.ArgumentParser("Print a list of days over a given number of weeks.")
    parser.add_argument(
        '-y',
        '--year',
        dest='year',
        type=int,
        default=now.year,
        help='Year (default is current year: {})'.format(now.year)
    )
    parser.add_argument(
        '-m',
        '--month',
        dest='month',
        type=int,
        default=now.month,
        help='Month (default is current month: {})'.format(now.month)
    )
    parser.add_argument(
        '-d',
        '--day',
        dest='day',
        type=int,
        default=now.day,
        help='Day (default is current day: {})'.format(now.day)
    )
    parser.add_argument(
        '-w',
        '--weeks',
        dest='weeks',
        type=int,
        default=14,
        help='Number of weeks. Default is 14.'
    )
    parser.add_argument(
        '-s',
        '--dows',
        dest='dows',
        default=None,
        metavar='Weekday',
        type=str,
        nargs='*',
        help='Weekdays we wish to print (e.g. Tue, Thu)'
    )
    args = parser.parse_args()
    main(args)
