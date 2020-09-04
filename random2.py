import random
import timeit

start = timeit.default_timer()

count = 0
for i in range(100):
    lucky_num = random.randint(5, 10)
    if lucky_num == 6:
        count += 1

print(count)
stop = timeit.default_timer()

print('Time: ', stop - start)
