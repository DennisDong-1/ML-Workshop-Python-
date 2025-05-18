# Threads - Smallest unit of a process that can be scheduled and executed independently
#           Think of a process as a factory and threads as the workers inside it
#           Threads share the same memory space but execute tasks independently

# Multithreading - Running multiple threads concurrently within a single process
#                  Can help do multiple things at once, good for I/O-bound tasks

import threading
import time

def greet():
    print("HELLO")
    time.sleep(2)
    print("GOOD LAD")

t1 = threading.Thread(target = greet)
t2 = threading.Thread(target = greet)

t1.start()
t2.start()

t1.join()
t2.join()

print("DONE!")

# Good for I/O bound (tasks that are slow cause of waiting(not computing)) tasks:
#     Downloading Files
#     Reading/Writing Files
#     Handling network requests
#     Waiting for APIs or databases

d1 = { i : i**2 for i in range(1, 5) }
print(d1)