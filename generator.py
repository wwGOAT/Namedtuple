import threading
import random


def calculate_square(number):
    result = number * number
    print(f"Square of: {number} is: {result}")


def run_th():
    numbers = [2, 4, 55, 6, 6]
    threads = []

    for _ in range(5):
        t = threading.Thread(target=calculate_square, args=(random.choice(numbers),))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
