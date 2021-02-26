"""

The knapsack problem is a problem in combinatorial optimization: Given a set of items,
each with a weight and a value, determine the number of each item to include in a collection so that
the total weight is less than or equal to a given limit and the total value is as large as possible.
It derives its name from the problem faced by someone who is constrained by a fixed-size knapsack
and must fill it with the most valuable items. The problem often arises in resource allocation where
the decision makers have to choose from a set of non-divisible projects or tasks
under a fixed budget or time constraint, respectively.
https://en.wikipedia.org/wiki/Knapsack_problem

function "knapsack(item_names, value, weight, capacity)" takes the items' names, values, weights,
and maximum weight that the backpack can carry as arguments.
Returned tuple containing array of names of selected items, total value of selected items and total weight.

"""


def knapsack01(item_names, value, weight, capacity):
    if (len(value) != len(weight)) or (len(value) != len(item_names)):
        raise RuntimeError('value, weight and item_names must be of same size.')
    for i in range(len(value)):
        if weight[i] < 0:
            raise RuntimeError('weights must be positive numbers.')
    return knapsack01_(item_names, value, weight, capacity)


def knapsack01_(item_names, value, weight, capacity):
    if (not item_names) or (capacity <= 0):
        return [], 0, 0
    names0, v0, w0 = knapsack01_(item_names[1:], value[1:], weight[1:], capacity)
    if capacity >= weight[0]:
        names0, v0, w0 = knapsack01_(item_names[1:], value[1:], weight[1:], capacity)
        names1, v1, w1 = knapsack01_(item_names[1:], value[1:], weight[1:], capacity - weight[0])
        if (v1 + value[0]) > v0:
            return [item_names[0]] + names1, v1 + value[0], w1 + weight[0]
    return names0, v0, w0
