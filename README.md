# COP4520Assignment2

To run this program first download the files minotaurBirthday.py and minotaurShowroom.py; save the files anywhere you desire. Next using a command prompt navigate to the directory you saved the file in. Once there, use the command following command to run the script:

For part 1:
python minotaurBirthday.py
For part 2:
python minotaurShowroom.p

# Part 1:
# Evaluation/Summary of approach

When approaching this problem I decided on using a strategy that involves choosing one thread to be the counter. One thread is able to be 100% certain that everyone has entered the labyrinth atleast once by counting empty platters each time the counter enters the labyrinth. This is done by only allowing the counter thread to refill the cupcake and only allowing each other thread to eat a cupcake once. This means that the counter will have to enter the labyrinth atleast N times, where N is the number of threads, but it a clear cut solution for the guests to determine when everyone has entered the labyrinth without communication.

# Proof of correctness, efficiency and experimental evaluation

This solution meets the criteria of the problem because it allows no communication between threads other than the platter being empty or not. The guests are randomly selected to enter the labyrinth allowing threads to enter the labyrinth multiple times. A lock is used to ensure that only one guest enters the labyrinth at a time. The use of random is likely critical to the runtime of the solution however it is required. 

# Part 2:
# Evaluation/Summary of approach

When approaching this problem I decided on using strategy #3, the implementation of a queue. This strategy has it's advantages in the way that all guests will be able to visit the showroom. Guests are able to enter the queue and explore the mansion until it is their turn to enter the showroom. The disadvantage of this strategy may be the overcomplication of the problem. The problem simply requires the implemenation of a strategy that allows guests to enter the showroom one at a time, using a queue involves extra steps that the strategies #1 and #2 do not require. When implementing this strategy I created a thread that would work as the dequeuer. That thread enters a dequeue function and will continually dequeue guests from the queue as long as not everyone has entered the showroom. The other threads which represent the guests enter a enqueue function and continually attempt to queue themselves for the showroom as long as they are not in the queue already and not everyone has entered the showroom.

# Proof of correctness, efficiency and experimental evaluation

This solution meets the criteria of the problem because it only allows one guest in the showroom at once. This is ensured through the use of a lock during enqueuing and the use of a solo thread working to dequeue the guests from the queue. This means that only one guest will be able to enter the showroom at a time as the dequeuer is working alone. This strategy allows the guests to enter the showroom multiple times as required as long as not every guest has entered the showroom. In terms of efficieny the solution may be lacking when compared to the simplicity of the other solutions, however it is a solid implemenation of a queue using multiple threads.
