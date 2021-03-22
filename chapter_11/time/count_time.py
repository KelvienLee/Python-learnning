import time


def for_loop():
    for i in range(10000):
        # print(i)
        pass


start = time.time()
for_loop()
end = time.time()
print(end - start)

start = time.perf_counter()
for_loop()
end = time.perf_counter()
print(end - start)


























