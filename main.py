# This is a simple counter

import time

__author__ = 'Listwas'
__version__ = '1.1'

# Wait for user input
input('Press ENTER to start counting\n Hit CTRL+C to stop the counter')

sec = 1
mins = 0
hour = 0
day = 0
week = 0
try:
    while True:
        print(f'                \r{week:02}:{day:02}:{hour:02}:{mins:02}:{sec:02}', end='\r')
        time.sleep(1)
        sec += 1
        if sec == 60:
            sec = 0
            mins += 1
        if mins == 60:
            mins = 0
            hour += 1
        if hour == 24:
            hour = 0
            day += 1
        if day == 7:
            day = 0
            week += 1

except KeyboardInterrupt:
    print(f"\rCounting lasted: {week}w {day}d {hour}h {mins}m {sec}s")
