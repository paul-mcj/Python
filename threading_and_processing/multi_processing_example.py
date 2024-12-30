from multiprocessing import Process, Value, Array, Lock
import time

# example func used with Values
def add_100(num, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            num.value += 1

# example func used with Array
def add_333(nums, lock):
    for i in range(333):
        time.sleep(0.01)
        for i in range(len(nums)):
            with lock:
                nums[i] += 1

def main():
    # ||| Values are used to create a shared memory object between different processes.
    # Below: "i" indicates integers, 0 is the starting value
    share_num = Value("i", 0)

    # we need to prevent race conditions (otherwise we do not guarantee one process modifies/reads the shared value exclusively, which is very bad and can lead to bugs), so we need a lock
    lock = Lock()

    # create two Value processes, so we can share the variable between them
    p1 = Process(target=add_100, args=(share_num, lock))
    p2 = Process(target=add_100, args=(share_num, lock))

    # now start the processes...
    p1.start()
    p2.start()

    # and make sure that these processes are finished execution before any subsequent code can be executed
    p1.join()
    p2.join()

    print(f"number at end is: {share_num.value}")

    # ||| Arrays are simply collections that store multiple Values.
    # Below: "d" indicates doubles
    shared_array = Array("d", [0.0, 100.0, 777.000])

    # create two Array processes, so we can share the variable between them
    p3 = Process(target=add_333, args=(shared_array, lock))
    p4 = Process(target=add_333, args=(shared_array, lock))

    # now start the processes...
    p3.start()
    p4.start()

    # and make sure that these processes are finished execution before any subsequent code can be executed
    p3.join()
    p4.join()

    print(f"Process Arrays: {shared_array[:]}")


if __name__ == "__main__":
    main()