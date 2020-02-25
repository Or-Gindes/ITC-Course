# Construct a function build_matrix(rows, cols) that gets 2 numbers representing
# number of rows and number of columns, and returns a two dimensional array (you should
# build a list of lists). The element value in the i-th row and j-th column of the array should be i*j.


def build_matrix(rows, cols):
    matrix = []                       # initialize empty matrix
    for i in range(1, rows+1):        # iterate over rows
        matrix.extend([[0] * cols])   # add a row list per number of rows
        for j in range(1, cols+1):    # iterate over columns
            matrix[i-1][j-1] = i * j  # build i-th row and j-column element as i * j
    return matrix

# print(build_matrix(5, 5))   # debugging output