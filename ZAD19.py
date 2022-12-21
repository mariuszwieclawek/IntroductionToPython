"""
Zaimplementuj prosty problem pięciu filozofów (z deadlockiem), następnie usuń deadlock.
"""

import threading
import time

class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, leftFork, rightFork):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        while self.running:
            time.sleep(10)
            print(f"Philosopher {self.index} try to eat\n")
            self.tryEat()

    def tryEat(self):
        fork1, fork2 = self.leftFork, self.rightFork
        while self.running:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print(f"Philosopher {self.index} can't eat\n")
            fork1, fork2 = fork2, fork1
        else:
            return
        self.eat()
        fork2.release()
        fork1.release()

    def eat(self):
        print(f"Philosopher {self.index} start eating\n")
        time.sleep(15)
        print(f"Philosopher {self.index} end eating\n")


if __name__ == '__main__':
    forks = [threading.Semaphore() for n in range(5)]

    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5])
                    for i in range(5)]

    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(60)
    Philosopher.running = False
    print("Ended\n")
