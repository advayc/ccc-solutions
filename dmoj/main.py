import sys
try:
    N = int(input())
    assert 2 <= N <= 100000, "N must be between 2 and 100000"

    for _ in range(N):
        line = input().strip()
        assert len(line.split()) == 4, "Each line must contain 4 integers"

        try:
            xi, yi, Ai, Bi = map(int, line.split())

            assert 1 <= xi <= 10**6 and 1 <= yi <= 10**6, "xi and yi must be between 1 and 10^6"

            assert abs(Ai) <= 2 * 10**12 and abs(Bi) <= 2 * 10**12, "Ai and Bi must be within the specified range"

        except ValueError:
            raise AssertionError("Invalid input: expected integers")

except AssertionError as e:
    print("error:",e)
    sys.exit(1)