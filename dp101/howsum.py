"""

function how_sum(target_sum, numbers) which takes in a target_sum
and an array of positive or zero numbers as arguments.
The function should return an array containing only one combination of elements such as they
add up to exactly the target_sum. If there is no combination, result is null.
Return only one possible combination.

function how_sum_all(target_sum, numbers) returns all the possible combinations.
It is based on repeated combinations of every possible length.

"""


def how_sum(target_sum, numbers):
    for n in numbers:
        if n < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    return how_sum_(target_sum, [n for n in numbers if (n > 0)])


def how_sum_(target_sum, numbers):
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    for n in numbers:
        a = how_sum_(target_sum - n, numbers)
        if a is not None:
            a.append(n)
            return a
    return None


def how_sum_m(target_sum, numbers):
    for n in numbers:
        if n < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    return how_sum_m_(target_sum, [n for n in numbers if (n > 0)], [])


def how_sum_m_(target_sum, numbers, memo):
    if target_sum in memo:
        return None
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    for n in numbers:
        a = how_sum_m_(target_sum - n, numbers, memo)
        if a is not None:
            a.append(n)
            return a
    memo.append(target_sum)
    return None


def how_sum_t(target_sum, numbers):
    for n in numbers:
        if n < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    tab = {}
    for a in range(target_sum+1):
        tab[a] = None
    tab[0] = []
    for a in range(target_sum):
        if tab[a] is not None:
            for n in numbers:
                if (a + n) <= target_sum and tab[a + n] is None:
                    tab[a + n] = tab[a] + [n]
    return tab[target_sum]


def how_sum_all(target_sum, numbers):
    for n in numbers:
        if n < 0:
            raise RuntimeError('numbers can only be positive or zero.')
    return how_sum_all_(target_sum, [n for n in numbers if (n > 0)])


def how_sum_all_(target_sum, numbers):
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    al = []
    for i in range(len(numbers)):
        a = how_sum_all_(target_sum - numbers[i], numbers[i:])
        if a is not None:
            if not a:
                al.append([numbers[i]])
            else:
                for elem in a:
                    b = elem + [numbers[i]]
                    al.append(b)
    if al:
        return al
    else:
        return None
