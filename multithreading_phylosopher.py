import random
import time
from threading import Thread

class Philosopher(Thread):

    def __init__(self, table, seat):
        self.table_ = table
        self.seat_ = seat
        self.left_chopstick_ = self.table_.left_chopstick(seat)
        self.right_chopstick_ = self.table_.right_chopstick(seat)
        self.meals_ = 0

    def eat(self):
        self.__acquire_chopsticks()
        self.__eat_with_chopsticks()
        self.__release_chopsticks()

    def think(self):
        time.sleep(random.random() * 5)  # think 0-5 seconds

    def run(self):
        while True:
            self.eat()
            self.think()

    def __acquire_chopsticks(self):
        while True:
            self.left_chopstick_.acquire()# wait operation on left fork
            locked = self.right_chopstick_.acquire(False) 
            
    def __eat_with_chopsticks(self):
        time.sleep(random.random() * 5)  # eat 0-5 seconds
        self.meals_ += 1

    def __release_chopsticks(self):
        self.right_chopstick_.release()
        self.left_chopstick_.release()

