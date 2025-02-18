mod = 1000000007
n = input().strip()

if n == "0":
    print(0)
elif n == "1":
    print(1)
else:
    mul = lambda a, b: [
        [ (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod ],
        [ (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod ]
    ]
    # identity matrix for 2x2
    identity = [[1, 0], [0, 1]]
    # fibonacci transition matrix
    fib_mat = [[1, 1], [1, 0]]
    st = [[0, 1]]
    
    final_mul = identity
    pow_mat = fib_mat
    
    # iterate over digits of n from right to left
    for digit in n[::-1]:
        v = int(digit)
        for _ in range(v):
            final_mul = mul(final_mul, pow_mat)
        new_pow = identity
        for _ in range(10):
            new_pow = mul(new_pow, pow_mat)
        pow_mat = new_pow

    # compute final answer as st * final_mul (only the first element is needed)
    ans0 = (st[0][0] * final_mul[0][0] + st[0][1] * final_mul[1][0]) % mod
    print(ans0)