import time

print("Hello world!")

NUMBER = 99999
init_time = time.time()
for i in range(NUMBER):
    print("HELLO")

print(time.time() - init_time)