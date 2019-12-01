def calc_pi(n: int) -> float:
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(n):
        pi += operation * (numerator / denominator)
        denominator += 2;
        operation *= -1
    return pi


print(calc_pi(1000000))
