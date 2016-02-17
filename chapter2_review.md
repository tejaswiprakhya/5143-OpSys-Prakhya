# Chapter 2 Review Questions
Name: Tejaswi Prakhya
Course: 5143 Operating Systems
Date: 17 Feb 2016


## 1.	What are three objectives of an OS design?
 1.Convenience – To provide the user friendly interface for the ease of access.
 
 2.Flexibility – Must be easily customized according the present market conditions like upgrading, updating with the latest patches available in the market to fix the bugs/enhancements.
 
 3.Security – Must provide access to its resources only to authorized users, 

## 2. What is the kernel of an OS?

Kernel resides in OS when compared, for example OS is an atom and kernel is nucleus. Actually it is a memory space for handling the OS functions
It acts as a bus between the user applications and the hardware. 

## 3. What is multiprogramming?
In a multiprogramming system if there are one or more programs which are ready to execute/executing. Among those programs if a program is waiting for user interrupt/ performing I/O task that particular program can be interrupted and let other programs waiting in queue to be executed to reduce the CPU idle time and increase the CPU efficiency.

## 4.	What is a process?
It’s a task that was initiated.

## 5.	How is the execution context of a process used by the OS?
1.Contains the process elements

2.Created and manage by the operating system

3.Allows support for multiple processes

## 6.	List and briefly explain five storage management responsibilities of a typical OS.
1.PROCESS ISOLATION:
The OS needs to handle independent processes from interfering with each of their memory, both data and instructions.

2.AUTOMATIC ALLOCATION AND MANAGEMENT:
Programs should be dynamically allocated across the memory hierarchy as required. Allocation should be transparent to the programmer to avoid ambiguity
OS can achieve efficiency by assigning memory to jobs (if needed)

3.SUPPORT OF MODULAR PROGRAMMING:
Programmers must design the program in modules, and to create, destroy, and alter the size of modules dynamically.

4.PROTECTION AND ACCESS CONTROL:
Sharing of memory, at any level of the memory hierarchy, creates the potential for one program to address the memory space
of another. This is desirable when sharing is needed by particular applications.
At other times, it threatens the integrity of programs and even of the OS itself.
The OS must allow portions of memory to be accessible in various ways by
various users.

5.LONG-TERM STORAGE:
Programs/Applications requires means for storing data, after the computer has been turned off.

## 7.	Explain the distinction between a real address and a virtual address.
Physical address refers to the hardware address in physical memory which is provided by the hardware.A machine has one physical address. (Ex :MAC address) 
Virtual address is given by OS Kernel. OS divides physical memory into partitions. Each partition is given to each process which is called as virtual address space.

## 8.	Describe the round-robin scheduling technique.
•	In round robin scheduling algorithm, each process is going to be executed in the given time interval.
•	The given time interval is termed as Quantum or time-slice.
•	If a process is not executed in the given time period, the process gets terminated and will be added at the last of the list of processes to be executed. It doesn’t disturb the execution of next process. 
•	If the process is executed before the time interval, the next process starts executing wherein the CPU is not idle. 

## 9.	Explain the difference between a monolithic kernel and a microkernel.
MONOLITHIC KERNELS:
kernel consists of many modules which can be dynamically loaded and un-loaded. With this modular and dynamic approach, maintainability of kernel was made easier as only the required module needs to be loaded for a bug fix or for its enhancement. A monolithic kernel executes all the os instructions in the same address space to improve the performance of the system.

MICROKERNELS:

A microkernel runs most of the operating system's background processes in user space which reduces the size of kernel code and increases the stability of OS as we have the minimum code running in kernel, which is easy to maintain.

## 10.	What is multithreading?
Multithreading refers to the multiple threads which are executing concurrently within a single process

## 11.	List the key design issues for an SMP operating system.
In SYMMETRIC MULTIPROCESSOR (SMP)
kernel can execute only one processor at a time
The processor itself schedules the execution of process/threads from the available pool processes or threads. 
To execute multiple process in parallel, the kernel is constructed in such a way that it can handle multiple threads to execute which in turn complicates the OS. While executing in parallel, processors must not pick same process, it must be unique.
OS routines must be independence so that level of granularity for locking gives good performance

