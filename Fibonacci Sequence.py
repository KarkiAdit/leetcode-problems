# Qn. Solve the fibonacci sequence using recursion, n1 = 0, n2 = 1


# O(2^n) solution
def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


# Optimized memoized version, O(n) solution
def fibonacci(num: int, memo) -> int:
    if num in memo:
        return memo[num]
    if num == 0:
        return 0
    if num == 1:
        return 1
    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]
