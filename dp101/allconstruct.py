"""

function all_construct(target, word_bank) which accepts a target string and an array of strings.
Returned a 2d array indicating all the unique ways to construct the target with the words in the wordBank.
Returned None if there's no way.
case sensitive version.

"""


def all_construct(target, word_bank):
    return all_construct_(target, [w for w in word_bank if (w != '')])


def all_construct_(target, word_bank):
    if target == '':
        return []
    sols = []
    for word in word_bank:
        if target.startswith(word):
            a = all_construct_(target[len(word):], word_bank)
            if a is not None:
                if not a:
                    sols.append([word])
                else:
                    for el in a:
                        el = [word] + el
                        sols.append(el)
    if not sols:
        return None
    else:
        return sols


def all_construct_m_(target, word_bank, memo):
    if target in memo:
        return memo[target]
    elif target == '':
        return []
    sols = []
    for word in word_bank:
        if target.startswith(word):
            a = all_construct_m_(target[len(word):], word_bank, memo)
            if a is not None:
                if not a:
                    sols.append([word])
                else:
                    for el in a:
                        el = [word] + el
                        sols.append(el)

    if not sols:
        memo[target] = None
        return None
    else:
        memo[target] = sols
        return sols


def all_construct_m(target, word_bank):
    return all_construct_m_(target, [w for w in word_bank if (w != '')], {})
