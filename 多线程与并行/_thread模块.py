import time
import datetime
import _thread

date_time_format = "%H:%M:%S"


def get_time_str():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, date_time_format)


def thread_function(thread_id):
    print("Thread %d\t start at %s" % (thread_id, get_time_str()))
    print("Thread %d\t sleeping" % thread_id)
    time.sleep(4)
    print("Thread %d\t finish at %s" % (thread_id, get_time_str()))


def main():
    print("Main thread start at %s" % get_time_str())
    for i in range(5):
        _thread.start_new_thread(thread_function, (i,))
        time.sleep(1)
    time.sleep(6)
    print("Main thread finish at %s" % get_time_str())


if __name__ == "__main__":
    main()
