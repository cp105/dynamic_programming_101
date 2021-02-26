"""

function "can_sum(target_sum, numbers)" takes in a targetSum
and an array of positive numbers as arguments. numbers elements can be used as many times as needed.
The function should return a boolean indicating whether or not it is possible to
generate the targetSum using numbers from the array.
Input numbers can only be positive or zero.

"""


def can_sum(target_sum, numbers):
    for i in numbers:
        if i < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    return can_sum_(target_sum, [a for a in numbers if (a > 0)])


def can_sum_(target_sum, numbers):
    if target_sum == 0:
        return True
    elif target_sum < 0:
        return False
    for i in numbers:
        ret = can_sum_(target_sum-i, numbers)
        if ret is True:
            return True
    return False


def can_sum_m_(target_sum, numbers, memo):
    if target_sum == 0:
        return True
    elif target_sum < 0:
        return False
    elif target_sum in memo:
        return memo[target_sum]
    for i in numbers:
        ret = can_sum_m_(target_sum-i, numbers, memo)
        if ret is True:
            return True
    memo[target_sum] = False
    return False


def can_sum_m(target_sum, numbers):
    for i in numbers:
        if i < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    return can_sum_m_(target_sum, [a for a in numbers if (a > 0)], {})


def can_sum_t(target_sum, numbers):
    for i in numbers:
        if i < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    tab = {}
    for i in range(target_sum+1):
        tab[i] = False
    tab[0] = True
    for i in range(target_sum+1):
        if tab[i] is True:
            for n in numbers:
                if i + n <= target_sum:
                    tab[i + n] = True
    return tab[target_sum]
