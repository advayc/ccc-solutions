# find factorial of number n using recursion
# recusion always starts with a base case then calls function else base case is not true

def factorial(n: int):
    if n == 1: # base case
        return 1
    else:
        return n * factorial(n-1)# factorial does n * n-1
                        # requires factorial function call so it does infinitly till base case is true
    
n = int(input('factorial: '))
print(factorial(n))

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
print(Fibonacci(N))
