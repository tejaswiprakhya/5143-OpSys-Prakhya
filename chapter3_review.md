# Chapter 3 Review Questions

Name: Tejaswi Prakhya

Course: 5143 Operating Systems

Date: 02 Mar 2016

## Question 1
3.4 What does it mean to preempt a process?

A process will be preempted when an other process with high priority has just become ready.
The other reason for a process to be preempted is when a process time slice is expired.

## Question 2
3.5 What is swapping and what is its purpose?

For the efficient management of memory, if there is a shortage of memory for a process to get executed which is in ready state, then the pages of the least active process 
will be swappped out of device, to free memory for process that is waiting.

## Question 3
3.9 List three general categories of information in a process control block.
Process control block has information of
-> Name of the process

-> State of the process

-> Resources allocated for the process

-> Memory used/allocated for the process

-> Process scheduling information

-> Process Id (PId ) of the process

-> I/O devices used by the process.

## Question 4
3.10 Why are two modes (user and kernel) needed?

In a multi user computer, if every user/program has complete access to CPU, main memory (unlimited access to all) then every user has access 
to all the available data. To overcome that scenario, the CPU has two privelages.

Kernel mode:Direct access to hardware,memory and Input/Output devices.

User mode : Access to limited set of instructions. Most of the user applications run in user mode.

## Question 5
3.12 What is the difference between an interrupt and a trap?

Interrupt are caused by external/hardware devices.

Trap is caused by software interrupt, its a high priority one which cannot be masked like as interrupts.

## Question 6
3.13 Give three examples of an interrupt.

-> Breaking the flow of executuion / running process from a keyboard by a key press.

-> errors ina program like divie by zero, array index out of bounds.

-> OS uses interrupts for multitasking.

## Question 7
3.14 What is the difference between a mode switch and a process switch?

A process switch is called when a processor switches from one process to another. 
This causes the contents of the cpu registers and instruction pointer to be saved. The registers and instruction pointer for 
the new task will then be loaded into the processor and execution of the new process will start/resume. The old program which is no 
longer executing, it's state is saved in memory, the kernel decides when to execute it again. 

A mode switch (Kernel/user mode) referred to when the cpu changes privilege levels. The kernel works at a higher privilege than a standard
user task.The process which requires high level of permissions, direct access to hardware gets executed in kernel mode and most of the user applications 
gets executed in user mode.  The processor uses these modes to protect the 
OS from misbehaving or malicious programs, as well as controlling concurrent access to ram, io devices,etc.
