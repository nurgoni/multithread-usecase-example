import queue
import threading
import time


# create thread safe queue
q = queue.Queue()

# the worker function that processes items from the queue
def worker_thread(name):
    while True:
        try:
            # get a task from the queue
            task = q.get()
            if task is None:    # sentinel value to signal exit
                break

            print(f"Thread {name} processing task: {task}")

            # simulate some work (e.g. I/O operation)
            time.sleep(1)
            print(f"Thread {name} finished task: {task}")

            # signal that the task is done
            q.task_done() 
            
        except queue.Empty:
            continue


# list of tasks to be added to the queue
tasks = ["task1", "task2", "task3", "task4", "task5"]
num_worker_threads = 3
threads = []

# create and start worker threads
for i in range(num_worker_threads):
    t = threading.Thread(
        target=worker_thread,
        args=(f"Worker-{i+1}",)
    )
    t.start()
    threads.append(t)

# add tasks to the queue (Producer)
for task in tasks:
    q.put(task)

# wait until all tasks in the queue are processed
q.join()

# stop the worker threads using sentinel values
for _ in range(num_worker_threads):
    q.put(None)

# wait for all threads to terminate
for t in threads:
    t.join()

print("All tasks processed and threads terminated.")
