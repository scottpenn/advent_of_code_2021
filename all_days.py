import timeit
import runpy
import sys

# Updated to the latest day completed.
today = 12

# Times the execution of a given day's solution
def run_day(day):
    print(f'Running Day {day:02d}')

    start = timeit.default_timer()

    runpy.run_path(f'days/day_{day:02d}/solution.py')

    stop = timeit.default_timer()

    print(f'Day {day:02d} Time: {stop - start:05f}s\n')

# Check for command line argument
if len(sys.argv) > 1:
    try:
        day = int(sys.argv[1])
        if today < day < 1:
            raise
        else:
            run_day(day)
    except:
        print(f'Day argument must be an integer between 1 and {today}')
# With no arguments, run all days
else:
    for day in range(1, today + 1):
        run_day(day) 