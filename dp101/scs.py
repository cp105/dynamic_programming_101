
"""

A shortest common super sequence (SCS) is a common super sequence of minimal length.
In the shortest common super sequence problem, two sequences X and Y are given, and the task is to
find a shortest possible common super sequence of these sequences.
In general, an SCS is not unique.
https://en.wikipedia.org/wiki/Shortest_common_supersequence_problem

function "scs(sq1, sq2)" takes in two sequences of numbers as arguments.
The function returns the shortest common super sequence of sq1 and sq2.

"""


def scs(sq1, sq2):
    return scs_(sq1, sq2, {})


def scs_(sq1, sq2, memo):
    if (len(sq1), len(sq2)) in memo:
        return memo[(len(sq1), len(sq2))]
    elif not sq1:
        return [el for el in sq2]
    elif not sq2:
        return [el for el in sq1]
    elif sq1[0] == sq2[0]:
        return [sq1[0]] + scs_(sq1[1:], sq2[1:], memo)
    a = [sq1[0]] + scs_(sq1[1:], sq2, memo)
    b = [sq2[0]] + scs_(sq1, sq2[1:], memo)
    if len(a) < len(b):
        memo[(len(sq1), (len(sq2)))] = a
        return a
    else:
        memo[(len(sq1), (len(sq2)))] = b
        return b
