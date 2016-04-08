# Assignment

#####Name: Tejaswi Prakhya

#####Course: 5143 Operating Systems

#####Date: 08 Apr 2016

#####Mustang Id : M20229037

## 1.Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.

Thread1.py has two threads A & B which are independent of each other. so the threads gets executed independent of each other and prints the value.
While in Thread2.py, both threads A & B are sharing a global variable "shared counter". The threads are dependent.


## 2.After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?

Yes, After running Thread3.py it fixed the problems that occured in Threads2.py.
In Thread2.py 'Shared Counter' is the global variable and both the threads A & B tried to access the shared variable at same time.
While in Thread3.py the 'Shared Counter' global variable is accessed by only one thread. The shared resource was synchronized by using lock.acquire() & lock.release()
The down side is dependency because of which it is causing latency.

## 3.Comment out the join statements at the bottom of the program and describe what happens.

If we comment out the join statements the main program gets completed before the child threads complete its execution.

## 4.What happens if you try to Ctrl-C out of the program before it terminates?

The external interrupt provided by end user using Ctrl-C has no effect. The program doesnt gets interrupted.

## 5.Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.

As there is no locking of Shared Counter there is a race condition. The IF statement value gets varied as the shared counter variable is used by both the threads.

## 6.Does uncommenting the lock operations clear up the problem in question 5?
Yes, by uncommenting the lock operations will clear up the problem in question 5.
As the shared counter value is locked, the IF statement behaves as expected.
