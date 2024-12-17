# creating threads is almost exactly the same as creating processes (see "basic_processing.py")
# NOTE: threads share the same memory space, thus they have access to the same data and makes sharing it simple.

from threading import Thread, Lock
import time

# define global variable for sharing data between threads
database_value = 0

# global function wants to take in a lock to prevent race conditions (more on this below)
def increase(lock):
    global database_value

    # the current thread invoking this function "holds the lock" passed in and is the only thread that has exclusive access to the section of code. Other threads *can* execute this function's code, but none of them will be able to do anything between acquiring and releasing a lock -- they pause function execution waiting for the current thread to be done.
    lock.acquire()

    # dummy code to simulate database data
    local_copy = database_value

    # processing (+fabricate wait time for demo purposes)
    local_copy += 1
    time.sleep(0.1)

    # write new value to database
    database_value = local_copy

    # NOTE: you must remember to always release a lock, otherwise it will lock a thread and block the usage of other ones
    lock.release()

    # Thus, anytime a thread uses this function, it is able to safely update the database value without having to worry about it being changed incorrectly by other threads. This is all because of locking!

def main():
    # if the program didn't have a lock (and thus, both thread_1 and thread_2 below didn't have any arguments) then there would be a race condition -- thread_1 would first call the increase function and process the simulated database value, then thread_2 afterwards. Since there is a simulated sleep timer (which is a fair real world example of wait time) there is a pause long enough that when thread_2 also invokes the increase function, the value hasn't yet been changed by thread_1. Thus, we get an "end value" printed of 1 when we expect 2.
    # Locks are needed to "stop" other threads from doing something while the current one can do its job, then after releasing the lock the next thread can do its thing, and so on. 
    # Essentially: A Lock in threading ensures only one thread at a time can execute a specific section of code. The Lock ensures that a resource or critical section is accessed one thread at a time to prevent race conditions or inconsistent states.
    l = Lock()

    print("start value: ", database_value)

    thread_1 = Thread(target=increase, args=(l,))
    thread_2 = Thread(target=increase, args=(l,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("end value: ", database_value)


if __name__ == "__main__":
    main()