import _thread
import datetime
import time

date_time_format = "%H:%M:%S"


def get_time_str():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, date_time_format)


def thread_function(thread_id, lock):
    print("Thread %d\t start at %s" % (thread_id, get_time_str()))
    print("Thread %d\t sleeping" % thread_id)
    time.sleep(4)
    print("Thread %d\t finish at %s" % (thread_id, get_time_str()))
    lock.release()


def main():
    locks = []
    for i in range(5):
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in range(5):
        _thread.start_new_thread(thread_function, (i, locks[i]))
        time.sleep(1)
    for i in range(5):
        while locks[i].locked():
            time.sleep(1)
    print("Main thread finish at %s" % get_time_str())


if __name__ == "__main__":
    main()
