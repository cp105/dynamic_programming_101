"""

function "count_construct(target, word_bank)" which accepts a target string and an array of strings.
Returned a value indicating in how many unique ways can we construct the target with the words in the wordBank.
Returned zero if there's no way.

"""

"""

function all_construct(target, word_bank) which accepts a target string and an array of strings.
Returned a 2d array indicating all the unique ways to construct the target with the words in the wordBank.
Returned None if there's no way.
case sensitive version.

"""


def count_construct(target, word_bank):
    return count_construct_(target, [w for w in word_bank if (w != '')])


def count_construct_(target, word_bank):
    if target == '':
        return 1
    counter = 0
    for word in word_bank:
        if target.startswith(word):
            counter += count_construct_(target[len(word):], word_bank)
    return counter


def count_construct_m_(target, word_bank, memo):
    if target in memo:
        return memo[target]
    elif target == '':
        return 1
    counter = 0
    for word in word_bank:
        if target.startswith(word):
            counter += count_construct_m_(target[len(word):], word_bank, memo)
    memo[target] = counter
    return counter


def count_construct_m(target, word_bank):
    return count_construct_m_(target, [w for w in word_bank if (w != '')], {})
