# creating threads is almost exactly the same as creating processes (see "basic_processing.py")
# NOTE: threads share the same memory space, thus they have access to the same data and makes sharing it simple.

from threading import Thread
import time

# define global variable for sharing data between threads
database_value = 0

def increase():
    global database_value

    # dummy code to simulate database data
    local_copy = database_value

    # processing + fabricate wait time
    local_copy += 1
    time.sleep(0.1)

    # write new value to database
    database_value = local_copy

def main():
    print("start value: ", database_value)

    thread_1 = Thread(target=increase)
    thread_2 = Thread(target=increase)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("end value: ", database_value)


if __name__ == "__main__":
    main()