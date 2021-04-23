# This is a simple counter

import time

__author__ = 'Listwas'

# Wait for user input
input('Press ENTER to start counting\n Hit CTRL+C to stop the counter')

counter = 1
try:
    while True:
        print(counter, end='\r')
        time.sleep(1)
        counter += 1
except KeyboardInterrupt:
    print("\rCounting lasted: ", str(counter) + "s")
