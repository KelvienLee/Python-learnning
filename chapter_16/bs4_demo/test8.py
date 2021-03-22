from datetime import datetime
from time import sleep

for i in range(10):
    for j in range(1, i+1):
        s = i * j
        print(f"{j} * {i} = {s}", end=' ')
    print('\n')

for i in range(10):
    print(datetime.now())
    print(i)
    sleep(0.5)

print('')

