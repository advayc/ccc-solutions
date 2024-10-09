import time
start_time = time.time()
end_time = time.time()
execution_time = end_time - start_time

def Factorial(n: int):
    if n == 1: # base case
        return 1
    else:
        return n * Factorial(n-1)# factorial does n * n-1
                        # requires factorial function call so it does infinitly till base case is true
n = int(input('factorial of: '))
print(Factorial(n))
print(f"Execution time: {execution_time} seconds")
