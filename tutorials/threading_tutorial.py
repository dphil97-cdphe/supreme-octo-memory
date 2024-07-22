from time import sleep, perf_counter
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def duration(start_time, end_time):

    print(f"It took {end_time - start_time: 0.2f} secs to complete.")

def task(id=None):

    print(f"Starting a task {id}...")
    
    # CPU is idle for 1 second
    sleep(1)

    print(f"Task {id} done.")

def thread_example():

    start_time = perf_counter()

    # Create 2 new threads
    t1 = Thread(target=task)
    t2 = Thread(target=task)

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to complete
    t1.join()
    t2.join()

    end_time = perf_counter()

    duration(start_time, end_time)

def arguments_to_threads():
    start_time = perf_counter()

    # Start 10 threads
    threads = []
    for n in range(1,11):
        t = Thread(target=task, args=(n,))
        threads.append(t)
        t.start()

    # Wait for threads to complete
    for t in threads:
        t.join()

    end_time = perf_counter()

    duration(start_time, end_time)


def thread_pool():

    start_time = perf_counter()

    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(task, 1)
        f2 = executor.submit(task, 2)

        print(f1.result())
        print(f2.result())

    end_time = perf_counter()

    duration(start_time, end_time)

def thread_pool_map():
    start_time = perf_counter()

    with ThreadPoolExecutor() as executor:
        results = executor.map(task, [1,2])
        for result in results:
            print(result)

    end_time = perf_counter()

    duration(start_time, end_time)

if __name__ == "__main__":
    thread_pool_map()