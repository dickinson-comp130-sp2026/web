import time

# A certain computer virus is able to create new versions of itself very rapidly. The number of replicas r of the virus after n seconds is given by a recursive formula r(n). When n=1, there are two replicas, so r(1)=2. When n=2, there are 5 replicas, so r(2)=5. For larger values of n, the formula for the number of replicas is r(n) = 3*r(n-2) + r(n-1).

def r(n):
    if n == 1:
        return 2

    if n == 2:
        return 5

    return 3*r(n-2) + r(n-1)


def r_memo(n, known):
    assert isinstance(n, int)
    assert n >= 1
    if n in known:
        return known[n]
    if n == 1:
        result = 2
    elif n == 2:
        result = 5
    else:  # n>=3
        result = 3*r_memo(n-2, known) + r_memo(n-1, known)
    known[n] = result
    return result


for i in range(35, 39):
    # Time the calculation without memoization
    start = time.perf_counter()
    val1 = r(i)
    t1 = time.perf_counter() - start
    print(f'i {i}, r(i) {val1} (time {t1:.6f}s)')

    # Time the calculation with memoization
    start = time.perf_counter()
    val2 = r_memo(i, {})
    t2 = time.perf_counter() - start
    print(f'i {i}, r_memo(i) {val2} (time {t2:.6f}s)')
