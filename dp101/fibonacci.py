
def fib(i):
    if i <= 0:
        return 0
    elif i == 1:
        return 1
    return fib(i-1) + fib(i-2)


def fib_m_(i, memo):
    if i <= 0:
        return 0
    elif i == 1:
        return 1
    elif i in memo:
        return memo[i]
    a = fib_m_(i-1, memo)
    memo[i-1] = a
    b = fib_m_(i-2, memo)
    memo[i-2] = b
    return a + b


def fib_m(i):
    return fib_m_(i, {})


def fib_t(i):
    tab = [i for i in range(i+1)]
    for a in range(2, i+1):
        tab[a] = tab[a-1] + tab[a-2]
    return tab[i]
