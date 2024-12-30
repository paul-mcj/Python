# Run code in parallel to speed up code with threading and processing

from multiprocessing import Process
import os
import time

# random demonstration function to show how to work with processes.
# NOTE: the multiprocessing library serializes functions using pickle, which means that it cannot properly create processes when passed in functions are defined locally (whereas these functions need to be shared between processes!). T
# ||| This is why if you are passing a function to a process, then define it in the global scope!
def square_nums(limit):
    for i in range(limit):
        i * i
        time.sleep(0.1) # keep each process alive just enough to see in task manager this being called for each process

def main():    
    processes = []
    num_processes = os.cpu_count() # my macbook air has 8
    print(num_processes)

    # create processes for each cpu
    for i in range(num_processes):
        # NOTE: Process constructor takes in one mandatory argument: a callable function/object. 
        # It may also need to take in a second important argument, which is a tuple that contains the actual arguments for the function passed in. If the function is non-argumentative, then no args are required.
        p = Process(target=square_nums, args=(100,))
        processes.append(p)

    # start each process
    for p in processes:
        p.start()

    # join the processes
    for p in processes:
        p.join()

    # NOTE: If you execute this script and look in task manager or activity manager, you can see that "python" processes are being created! You can identify the processes by their ID.

    # This will print only AFTER all processes have been configured
    print(f"All {num_processes} processes have been configured")


if __name__ == "__main__":
    main()