# A process pool is a collection of worker processes that can execute tasks concurrently. You create a pool of workers (processes) and assign them tasks.

from multiprocessing import Pool

def cube(num):
    return num * num * num

def main():
    # define pool
    pool = Pool()

    # make a list 0 - 9
    nums = range(10)

    # we apply each item in the iterable to the given function, and pool.map() will distribute the function calls across multiple processes in a pool allowing for parallel execution. 
    # The ".map()" function typically creates as many processes as available on the local machine, and can split the calls to the function across the processes in equal-sized "chunks"
    result = pool.map(cube, nums)

    # NOTE: need to make sure to close the pool
    pool.close()

    # and as always, pause execute of subsequent code in the program until all process pool tasks have been completed
    pool.join()

    print(result)

if __name__ == "__main__":
    main()