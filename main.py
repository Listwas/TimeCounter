# This is a simple counter

import time

__author__ = 'Listwas'

# Wait for user input
input('Wciśnij enter aby zacząć liczyć\n')

counter = 1
try:
    while True:
        print(counter)
        time.sleep(1)
        counter += 1
except KeyboardInterrupt:
    print("\nodliczanie trwało: ", str(counter) + "s")
