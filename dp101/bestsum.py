"""

function best_sum(target_sum, numbers) takes target_sum
and an array of positive or zero numbers as arguments.
The function should return the minimum length combination of elements that
add up to exactly the target_sum. Only one combination is returned.
If no combination is found the return value is None.

"""


def best_sum_(target_sum, numbers):
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    mx = []
    for n in numbers:
        a = best_sum_(target_sum - n, numbers)
        if a is not None:
            comb = a + [n]
            if not mx or (len(comb) < len(mx)):
                mx = comb
    if mx:
        return mx
    else:
        return None


def best_sum(target_sum, numbers):
    for n in numbers:
        if n < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    return best_sum_(target_sum, [n for n in numbers if (n > 0)])


def best_sum_m_(target_sum, numbers, memo):
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    mx = []
    for n in numbers:
        a = best_sum_m_(target_sum - n, numbers, memo)
        if a is not None:
            comb = a + [n]
            if not mx or (len(comb) < len(mx)):
                mx = comb
    memo[target_sum] = mx
    if mx:
        return mx
    else:
        return None


def best_sum_m(target_sum, numbers):
    for n in numbers:
        if n < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    return best_sum_m_(target_sum, [n for n in numbers if (n > 0)], {})


def best_sum_t(target_sum, numbers):
    for n in numbers:
        if n < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    tab = {}
    for i in range(target_sum + 1):
        tab[i] = None
    tab[0] = []
    for i in range(target_sum):
        if tab[i] is not None:
            for n in numbers:
                comb = tab[i] + [n]
                if (i + n) <= target_sum:
                    if tab[i + n] is None or (len(comb) < len(tab[i + n])):
                        tab[i + n] = comb
    return tab[target_sum]

