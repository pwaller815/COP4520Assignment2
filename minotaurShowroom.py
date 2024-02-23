# Parker Waller
# Assignment 2 Part 2
# COP 4520
# 2/22/24

import threading
import time

lock = threading.Lock()
queue = []
visited = set()

def enterShowroom(guestNum):
    with lock:
        print("Guest #" + str(guestNum) + " entered the showroom.")
        visited.add(guestNum)

def enqueue(numGuests, guestNum):
    while True:
        if len(visited) == numGuests:
                break
        with lock:
            if guestNum not in queue:
                    queue.append(guestNum)
                    print("Guest #" + str(guestNum) + " just joined the queue.")
        time.sleep(0.1)

def dequeue(numGuests):
    while True:
        time.sleep(0.1)
        if len(visited) == numGuests:
            break
        if len(queue) > 0:
            enterShowroom(queue.pop(0))
        
def main():
    numGuests = int(input("How many guests are attending?\n"))
    threads = []
    thr = threading.Thread(target=dequeue, args=(numGuests,))
    thr.start()
    threads.append(thr)
    for i in range(numGuests):
        thr = threading.Thread(target=enqueue, args=(numGuests, i+1))
        thr.start()
        threads.append(thr)
    
    for thr in threads:
        thr.join()
        
    print("All guests have visited the showroom.")

main()
