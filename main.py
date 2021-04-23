# This is a simple counter

import time

__author__ = 'Listwas'

# Wait for user input
input('Wciśnij enter aby zacząć liczyć\n')

counter = 1
while True:
    print(counter)
    time.sleep(1)
    counter += 1
