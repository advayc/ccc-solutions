import time
# find factorial of number n using recursion
# recusion always starts with a base case then calls function else base case is not true

'''
recursion should include...

A simple base case which we have a solution for and a return value. 
A way of getting our problem closer to the base case. 
    I.e. a way to chop out part of the problem to get a somewhat simpler problem. 
A recursive call which passes the simpler problem back into the method. 


recursion always passes complex problem decremented by 1 outside of the base case

decompose the problem into smaller parts
'''
# find Fibonacci sequence at term n

def Fibonacci(N: int):
    if N == 1:
        return 1
    elif N == 2:
        return 1
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

N = int(input())

start_time = time.time()
result = Fibonacci(N)
end_time = time.time()

execution_time = end_time - start_time

print(f"The Fibonacci number at position {N} is {result}")
print(f"Execution time: {execution_time} seconds")