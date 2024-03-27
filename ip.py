import time
from datetime import datetime


def task_1(x):
    time.sleep(1)
    return x ** 2


def task_2(x):
    time.sleep(1)
    return x ** 3


def task_3(x):
    time.sleep(1)
    return x ** 4


def main(x):
    yield task_1(x)
    yield task_2(x)
    yield task_3(x)


if __name__ == "__main__":
    print(datetime.now().time())
    for i in main(5):
        print(i)
    print(datetime.now().time())
