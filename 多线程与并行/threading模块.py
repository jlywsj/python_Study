import time
import datetime
import threading


def get_time_str():
    now = datetime.datetime.now()
    date_time_format = "%H:%M:%S"
    return datetime.datetime.strftime(now, date_time_format)


def thread_function(thread_id):
    print("Thread %d\t start at %s" % (thread_id, get_time_str()))
    print("Thread %d\t sleeping" % thread_id)
    time.sleep(4)
    print("Thread %d\t finish at %s" % (thread_id, get_time_str()))


def main():
    print("Main thread start at %s" % get_time_str())
    threads = []
    for i in range(5):
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)

    for thread in threads:
        thread.start()
        time.sleep(1)

    for thread in threads:
        thread.join()

    print("Main thread finish at %s" % get_time_str())


if __name__ == "__main__":
    main()
