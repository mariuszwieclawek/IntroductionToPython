"""
Zaimplementuj wielowątkowe liczenie histogramu (monitorować wykonanie htop)
"""

import matplotlib.pyplot as plt
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

q = Queue(maxsize=3)
x = []


def histogram():
    while True:
        x.append(int(q.get()))
        plt.hist(x)
        plt.xlim([0, 100])
        plt.show()


def generate():
    while True:
        i = np.random.randint(0, 100, 1, int)
        q.put(i)


if __name__ == '__main__':
    with ThreadPoolExecutor() as exe:
        exe.submit(generate)
        exe.submit(histogram)
