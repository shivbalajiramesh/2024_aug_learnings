#https://www.youtube.com/watch?v=2ZwuKeL0aHs&list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm

import time
import threading


def sleeper(n, name):
    print(f'\n{name} going to sleep for {n} secs\n')
    time.sleep(n)
    print(f'{name} just woke up\n')
'''
t = threading.Thread(target = sleeper, name = 'Thread 1', args = (5, 'Thread 1'))

t.start()
t.join()

print('Hello World\n')
print('Hello World\n')
print('Hello World\n')
'''

#Multi Threading
start = time.time()

threads_list = []

for i in range(5):
    t = threading.Thread(target = sleeper, name = f'Thread {i}', args = (8-i, f'Thread {i}'))
    threads_list.append(t)
    t.start()

for t in threads_list:
    t.join()

end = time.time()

print('All the tasks have finished.\n')

print(f'Time taken: {end - start}')