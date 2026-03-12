import multiprocessing
import os
import time

def long_task(task_id):
    print(f"Process {task_id} started, PID: {os.getpid()}")

    for i in range(1, 6):
        print(f"Process {task_id}, step {i}/5, PID: {os.getpid()}")
        time.sleep(1)  # simulate long work

    print(f"Process {task_id} finished, PID: {os.getpid()}")


def main():
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=long_task, args=(i + 1,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes finished")


if __name__ == "__main__":
    main()