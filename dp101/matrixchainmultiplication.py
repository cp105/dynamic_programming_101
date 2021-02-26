
"""

Matrix chain multiplication (or the matrix chain ordering problem) is an optimization problem
concerning the most efficient way to multiply a given sequence of matrices.
The problem is not actually to perform the multiplications,
but merely to decide the sequence of the matrix multiplications involved.
https://en.wikipedia.org/wiki/Matrix_chain_multiplication

function mcm_max_cost(matrix_dims, matrix_names) takes the dimensions and names of the matrices as arguments.
The function returns the maximum cost to multiply the matrices, and a string representation of the
multiplications ordering.

example.
m_dims = [(10,5), (5,2), (2,20), (20,5), (5,5)]
print(mcm_max_cost(m_dims, ['a', 'b', 'c', 'd', 'e']))
>> (2700, '(((a x b) x c) x (d x e))')

m_dims = [(1000,30), (30,50), (50,6), (6,100), (100, 1)]
print(mcm_max_cost(m_dims, ['a', 'b', 'c', 'd', 'e']))
>> (6630000, '((((a x b) x c) x d) x e)')

"""


def mcm_max_cost(matrix_dims, matrix_names):
    if len(matrix_dims) != len(matrix_names):
        raise RuntimeError('matrix_dims and matrix_names must have same length.')
    for i in range(len(matrix_dims) - 1):
        if matrix_dims[i][1] != matrix_dims[i + 1][0]:
            raise RuntimeError('matrix dimensions must be consistent.')
    return mcm_max_cost_(matrix_dims, matrix_names, {})


def mcm_max_cost_(matrix_dims, matrix_names, memo):
    if len(matrix_dims) <= 1:
        return 0, matrix_names[0]
    elif tuple(matrix_dims) in memo:
        return memo[tuple(matrix_dims)]
    costs = list()
    sols = list()
    for mm_i in range(len(matrix_dims) - 1):
        curr_cost = matrix_dims[mm_i][0] * matrix_dims[mm_i][1] * matrix_dims[mm_i + 1][1]
        curr_mat = (matrix_dims[mm_i][0], matrix_dims[mm_i + 1][1])
        new_chain = matrix_dims[:mm_i] + [curr_mat] + matrix_dims[(mm_i + 2):]
        new_names = matrix_names[:mm_i] + ['(' + str(matrix_names[mm_i]) + ' x ' + matrix_names[mm_i + 1] + ')'] + matrix_names[(mm_i + 2):]
        cost, name = mcm_max_cost_(new_chain, new_names, memo)
        costs.append(curr_cost + cost)
        sols.append(name)
    idx = costs.index(max(costs))
    memo[tuple(matrix_dims)] = (costs[idx], sols[idx])
    return costs[idx], sols[idx]


def mcm_min_cost(matrix_dims, matrix_names):
    if len(matrix_dims) != len(matrix_names):
        raise RuntimeError('matrix_dims and matrix_names must have same length.')
    for i in range(len(matrix_dims) - 1):
        if matrix_dims[i][1] != matrix_dims[i + 1][0]:
            raise RuntimeError('matrix dimensions must be consistent.')
    return mcm_min_cost_(matrix_dims, matrix_names, {})


def mcm_min_cost_(matrix_dims, matrix_names, memo):
    if len(matrix_dims) <= 1:
        return 0, matrix_names[0]
    elif tuple(matrix_dims) in memo:
        return memo[tuple(matrix_dims)]
    costs = list()
    sols = list()
    for mm_i in range(len(matrix_dims) - 1):
        curr_cost = matrix_dims[mm_i][0] * matrix_dims[mm_i][1] * matrix_dims[mm_i + 1][1]
        curr_mat = (matrix_dims[mm_i][0], matrix_dims[mm_i + 1][1])
        new_chain = matrix_dims[:mm_i] + [curr_mat] + matrix_dims[(mm_i + 2):]
        new_names = matrix_names[:mm_i] + ['(' + str(matrix_names[mm_i]) + ' x ' + matrix_names[mm_i + 1] + ')'] + matrix_names[(mm_i + 2):]
        cost, name = mcm_min_cost_(new_chain, new_names, memo)
        costs.append(curr_cost + cost)
        sols.append(name)
    idx = costs.index(min(costs))
    memo[tuple(matrix_dims)] = (costs[idx], sols[idx])
    return costs[idx], sols[idx]
