# Parker Waller
# Assignment 2 Part 1
# COP 4520
# 2/18/24

import threading
import time
import random

lock = threading.Lock()
totalEaten = 0
cupcake = True
randomGuest = 0
event = threading.Event()

class guestThread(threading.Thread):
    def __init__(self, numGuests, guestNum):
        super().__init__()
        self.numGuests = numGuests
        self.guestNum = guestNum
        self.eaten = False

    def run(self):
        global totalEaten
        global cupcake
        global randomGuest
        while True:
            if randomGuest == self.guestNum:
                with lock:
                    if totalEaten >= self.numGuests:
                        if self.guestNum == 1 and not self.eaten:
                            continue
                        event.set()
                        break
                    if not self.eaten:
                        if cupcake:
                            print("Thread #" + str(self.guestNum) + " ate the cupcake")
                            self.eaten = True
                            cupcake = False
                    if self.guestNum == 1 and not cupcake:
                        print("The counter found an empty tray!")
                        totalEaten += 1
                        cupcake = True
                    randomGuest = random.randint(1, self.numGuests)

def main():
    t = time.time()
    numGuests = int(input("How many guests are attending?\n"))
    global randomGuest
    randomGuest = random.randint(1, numGuests)
    threads = []
    for i in range(numGuests):
        thr = guestThread(numGuests, i+1)
        thr.start()
        threads.append(thr)
    
    event.wait()  
    t = time.time() - t
    print("All guests have entered the labyrinth.")

main()
