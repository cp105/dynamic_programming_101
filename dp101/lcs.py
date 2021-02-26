"""

The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to
all sequences in a set of sequences (often just two sequences).
It differs from the longest common substring problem: unlike substrings, subsequences are not required to
occupy consecutive positions within the original sequences.
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

function "lcs(sq1, sq2)" takes in two sequences of numbers as arguments.
The function returns the longest common subsequence of sq1 and sq2.

"""


def lcs_(sq1, sq2, memo):
    if (len(sq1), len(sq2)) in memo:
        return memo[(len(sq1), len(sq2))]
    elif not sq1 or not sq2:
        return []
    elif sq1[0] == sq2[0]:
        return [sq1[0]] + lcs_(sq1[1:], sq2[1:], memo)
    a = lcs_(sq1, sq2[1:], memo)
    b = lcs_(sq1[1:], sq2, memo)
    if len(a) > len(b):
        memo[(len(sq1), len(sq2))] = a
        return a
    else:
        memo[(len(sq1), len(sq2))] = b
        return b


def lcs(sq1, sq2):
    return lcs_(sq1, sq2, {})
