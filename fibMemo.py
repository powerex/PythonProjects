from typing import Dict

memo = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


print(fib(500))
