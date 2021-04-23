# This is a simple counter

import time

__author__ = 'Listwas'

# Wait for user input
input('Press ENTER to start counting\n Hit CTRL+C to stop the counter')

sec = 1
mins = 0
try:
    while True:
        print(f'    \r{mins:02}:{sec:02}', end='\r')
        time.sleep(0.2)
        sec += 1
        if sec == 60:
            sec = 0
            mins += 1

except KeyboardInterrupt:
    print("\rCounting lasted: ", str(mins) + "m", str(sec) + "s")