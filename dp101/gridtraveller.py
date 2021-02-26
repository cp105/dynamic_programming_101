"""

function grid_traveler(n_rows, n_cols) which takes the number of columns, and rows of the grid as arguments.
The function should return the number of ways we can go from the top left corner of the grid to the bottom right one
(or vice versa, the number of ways remains the same).
It is only possible to move down or right.

"""


def grid_traveller_(n_rows, n_cols):
    if (n_rows <= 1) and (n_cols <= 1):
        return 1
    elif n_rows <= 1:
        return grid_traveller_(n_rows, n_cols - 1)
    elif n_cols <= 1:
        return grid_traveller_(n_rows - 1, n_cols)
    else:
        n_right = grid_traveller_(n_rows, n_cols - 1)
        n_down = grid_traveller_(n_rows - 1, n_cols)
        return n_down + n_right


def grid_traveller(n_rows, n_cols):
    if (n_rows < 0) or (n_cols < 0):
        raise RuntimeError('n_rows and n_cols must be positive or zero.')
    if (n_rows == 0) and (n_cols == 0):
        return None
    return grid_traveller_(n_rows, n_cols)


def grid_traveller_m_(n_rows, n_cols, memo):
    if (n_rows <= 1) and (n_cols <= 1):
        return 1
    elif n_rows <= 1:
        n = grid_traveller_m_(n_rows, n_cols - 1, memo)
        memo[(n_rows, n_cols - 1)] = n
        return n
    elif n_cols <= 1:
        n = grid_traveller_m_(n_rows - 1, n_cols, memo)
        memo[(n_rows - 1, n_cols)] = n
        return n
    else:
        n_right = grid_traveller_m_(n_rows, n_cols - 1, memo)
        memo[(n_rows, n_cols - 1)] = n_right
        n_down = grid_traveller_m_(n_rows - 1, n_cols, memo)
        memo[(n_rows - 1, n_cols)] = n_down
        return n_down + n_right


def grid_traveller_m(n_rows, n_cols):
    if (n_rows < 0) or (n_cols < 0):
        raise RuntimeError('n_rows and n_cols must be positive or zero.')
    if (n_rows == 0) and (n_cols == 0):
        return None
    return grid_traveller_m_(n_rows, n_cols, {})


def grid_traveller_t(n_rows, n_cols):
    if (n_rows < 0) or (n_cols < 0):
        raise RuntimeError('n_rows and n_cols must be positive or zero.')
    if (n_rows == 0) and (n_cols == 0):
        return None
    tab = [[0 for _ in range(n_cols + 1)] for _ in range(n_rows + 1)]
    tab[1][1] = 1
    for i in range(1, n_rows + 1):
        for j in range(1, n_cols + 1):
            tab[i][j] = tab[i][j] + tab[i - 1][j] + tab[i][j - 1]
    return tab[n_rows][n_cols]
