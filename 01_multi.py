import threading
import time

# GIL
def print_numbers():
    for i in range(1, 11):
        print(f"Thread: {threading.current_thread().name}, Number: {i} ")
        time.sleep(0.2)  # just to make the output easier to see


def main():
    threads = []

    for i in range(3):
        t = threading.Thread(target=print_numbers, name=f"Worker-{i+1}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads finished")


if __name__ == "__main__":
    main()