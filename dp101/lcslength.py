"""

The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to
all sequences in a set of sequences (often just two sequences).
It differs from the longest common substring problem: unlike substrings, subsequences are not required to
occupy consecutive positions within the original sequences.
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

function "lcs_length(sq1, sq2)" takes in two sequences of numbers as arguments.
The function should return the number of elements of the longest common subsequence of sq1 and sq2.

"""


def lcs_length_(sq1, sq2, memo):
    if (len(sq1), len(sq2)) in memo:
        return memo[(len(sq1), len(sq2))]
    elif not sq1 or not sq2:
        return 0
    elif sq1[0] == sq2[0]:
        return lcs_length_(sq1[1:], sq2[1:], memo) + 1
    a = max(lcs_length_(sq1, sq2[1:], memo), lcs_length_(sq1[1:], sq2, memo))
    memo[(len(sq1), len(sq2))] = a
    return a


def lcs_length(sq1, sq2):
    a = lcs_length_(sq1, sq2, {})
    return a


def lcs_length_t(sq1, sq2):
    if (len(sq1) == 0) or (len(sq2) == 0):
        return 0
    tab = [[0 for _ in range(len(sq1))] for _ in range(len(sq2))]
    for i in range(len(sq2)):
        for j in range(len(sq1)):
            i_ = i - 1
            j_ = j - 1
            if sq1[j] == sq2[i]:
                if (i_ < 0) or (j_ < 0):
                    tab[i][j] = 1
                else:
                    tab[i][j] = tab[i_][j_] + 1
            else:
                if (i_ < 0) and (j_ < 0):
                    tab[i][j] = 0
                elif i_ < 0:
                    tab[i][j] = tab[i][j_]
                elif j_ < 0:
                    tab[i][j] = tab[i_][j]
                else:
                    tab[i][j] = max(tab[i][j_], tab[i_][j])
    return tab[(len(sq2)-1)][(len(sq1)-1)]
