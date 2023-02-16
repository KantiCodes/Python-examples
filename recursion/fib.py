def fib(n):
    print(f"calling for: {n}")
    if n == 1 or n == 2:
        return 1
    return (fib(n-1) + fib(n-2))

def fib_memo(n, memo):
    print(f"calling for: {n}")
    if n == 1 or n == 2:
        memo[n] = 1
        print(f"coming back from {n}")
        return 1
    if memo[n] != -1:
        print(f"returning from memo{n}")
        print(f"coming back from {n}")
        return memo[n]
    print(f"Calculating for {n}  <----")
    print("left")
    memo[n-1] = fib_memo(n-1, memo)
    print("right")
    memo[n-2] = fib_memo(n-2, memo)
    print(f"coming back from {n}")
    return memo[n-1] + memo[n-2]

def test():
    assert fib(1) == 1 and fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8


  

# fib(5)
# calling for: 5
# calling for: 4
# calling for: 3
# calling for: 2
# calling for: 1
# calling for: 2
# calling for: 3
# calling for: 2
# calling for: 1

fib(5)

    #                            5
    #                4                      3
    #       3              2            2       1
    #   2       1      


# With memo we avoid browing the "3 tree"
fib_memo(5, [-1]*(5+1))
    #                            5
    #                4                      3
    #       3              2
    #   2       1   