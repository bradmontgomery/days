#!/usr/bin/env python

import argparse
import calendar

from datetime import date, datetime
from itertools import zip_longest


def _grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def get_days(year, month, day, days, weeks=14):
    """Print some days of the calendar sequentially.

    - year: starting year, e.g. 2018
    - month: integer month, e.g. 1 for January
    - day: day of the month, e.g. 20
    - days: A list of days of the week in which we're interested. These should
      be written as the first 3 chars; default is ['Tue', 'Thu']
    - weeks: Number of weeks we print; default is 14

    """
    results = []

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
    dows = args.dows or ['Tue', 'Thu']
    results = get_days(args.year, args.month, args.day, dows, weeks=args.weeks)
    if args.chunk:
        results = _grouper(results, len(dows))
        for group in results:
            for day in group:
                if day is not None:
                    print(day[:10])
            print("-" * 10)
    else:
        for day in results:
            print(day[:10])


def cli():
    now = datetime.now()

    parser = argparse.ArgumentParser("Print a list of days over a given number of weeks.")
    parser.add_argument(
        '--start-date',
        dest='start_date',
        type=str,
        default=None,
        help='Start date in YYYY-MM-DD format (overrides -y, -m, -d if provided)'
    )
    parser.add_argument(
        '-y',
        '--year',
        dest='year',
        type=int,
        default=now.year,
        help='Starting year (default: {})'.format(now.year)
    )
    parser.add_argument(
        '-m',
        '--month',
        dest='month',
        type=int,
        default=now.month,
        help='Starting month (default: {})'.format(now.month)
    )
    parser.add_argument(
        '-d',
        '--dom',
        dest='day',
        type=int,
        default=now.day,
        help='Day of month to start (default: {})'.format(now.day)
    )
    parser.add_argument(
        '-n',
        '--num-weeks',
        dest='weeks',
        type=int,
        default=14,
        help='Number of weeks to print (default: 14)'
    )
    parser.add_argument(
        '-w',
        '--weekdays',
        '--on',
        dest='dows',
        default=None,
        metavar='WEEKDAY',
        type=str,
        nargs='+',
        help='Weekdays to print (e.g., Tue Thu) (default: Tue Thu)'
    )
    parser.add_argument(
        '-g',
        '--group',
        dest='chunk',
        action='store_true',
        default=False,
        help="Group output by weeks"
    )
    args = parser.parse_args()
    
    # Handle --start-date if provided
    if args.start_date:
        try:
            start = datetime.strptime(args.start_date, '%Y-%m-%d')
            args.year = start.year
            args.month = start.month
            args.day = start.day
        except ValueError:
            parser.error('--start-date must be in YYYY-MM-DD format')
    
    main(args)


if __name__ == "__main__":
    cli()
