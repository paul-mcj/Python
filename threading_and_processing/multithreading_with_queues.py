# Queues are thread and process safe collections in FIFO format (ex. a lineup at a coffee shop)
from threading import Thread, Lock, current_thread
from queue import Queue

def worker(queue, lock):
    # infinite loop is able to correctly end because of the set thread.daemon = True
    while True:
        # get the next item in the queue (ex. serve the next customer)
        value = queue.get()

        # processing "with" keyword is basically the same as doing lock.acquire, and finishing it with lock.release. This prevents inequalities of state.
        with lock:
            print(f"currently in {current_thread().name} with value: {value}")

        # NOTE: tells the program we are done processing this object, and can continue. This is important since queue.put() considers new items unfinished tasks.
        queue.task_done()

def main():
    q = Queue()

    # the front of the queue is the *last* item in the queue (like a lineup, every new person is added at the end, so it "pushes" the lineup forward):
    # q.put(1)
    # q.put(2)
    # q.put(3)
    # first = q.get()
    # print(first) # 1

    num_threads = 10
    lock = Lock()

    # create threads
    for _ in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True # Daemon threads are typically used for background tasks that should not prevent the program from exiting (ex. monitoring tasks). Setting the daemon thread to True will automatically terminate when the main program exits.
        thread.start()

    # add 20 elements to our queue for demo purposes
    for i in range(1, 21):
        # when an item is added to a queue, it is automatically considered an unfinished task
        q.put(i)

    # queue.join() blocks the main thread until all tasks in the queue have been marked as done (i.e., until task_done() has been called for each item).
    q.join()

    print("end...")

if __name__ == "__main__":
    main()