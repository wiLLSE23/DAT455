"""matrix
This modules provides functions for matrix operations. The matrices are assumed to be lists of lists of numbers.

This file can also be imported as a module and contains the following
functions:

    * transpose - transposes a matrix and returns the results. That is make the rows columns and the columns rows.
    * powers - returns a matrix of a given vector and the same vector raised to the first and second power given as parameters.
    * matmul - multiplies to matrices together and returns the result.
    * invert - prints the top most n words in a dictionary of frequencies.
    * loadtxt - load existing x and y values from a file.
"""
    
def _isValidMatrix(matrix):
    """Tests if a matrix is valid that is a non-empty list of non-empty lists.

    Parameters
    ----------
    matrix : list
        a list representing a matrix

    Returns
    -------
    boolean
        True if matrix is valid, False otherwise
    """
    if not isinstance(matrix, list):
        return False
    if not matrix:
        return False
    if not isinstance(matrix[0], list):
        return False
    return True

def transpose(matrix):
    """Returns a new matrix where the rows are turned into columns and the columns into rows.

    Parameters
    ----------
    matrix : list
        a list representing a matrix

    Returns
    -------
    list
        a transposed matrix
    """
    if _isValidMatrix(matrix) is False:
        print("Error in tranpose: invalid matrix")
        return []

    old_rows = len(matrix)
    old_cols = len(matrix[0])

    #creates empty matrix with old_cols as number of rows
    transposed_matrix = [ [] for _ in range(old_cols) ]

    #each row in matrix is added to column in
    for i in range(old_rows):
        for j in range(old_cols):
            transposed_matrix[j].append(matrix[i][j])

    return transposed_matrix

def powers(vector, first_power, second_power):
    """Returns a matrix of a given vector and the same vector raised to the first and second power given as parameters.

    Parameters
    ----------
    vector : list
        a list of numbers
    first_power : number
        the first power to raise the vector to
    second_power : number
        the second power to raise the vector to

    Returns
    -------
    list
        a list of the vector and the vector raised to the first and second power
    """
    if not len(vector) == []:
        print("Error in power: vector is empty")
        return []

    if not (first_power in [0,1,2] and second_power in [0,1,2]):
        print("Error in power: powers must be 0, 1, or 2")
        return [[]]

    #return matrix
    power_matrix = []
    #vector of all powers
    power_vector = []

    #make sure array contains the vector of all unique powers ranging from first_power to second_power where all powers are between 0 and 2
    for i in range(first_power, second_power+1):
        power_vector.append(i)
      
    #create matrix of powers
    for component in vector:
        power_matrix.append([component**i for i in power_vector])

    return power_matrix

def matmul(matrix1, matrix2):
    """Computes and returns the product of two matrices.

    Parameters
    ----------
    matrix1 : list
        a list representing a matrix. Factor 1
    matrix2 : list
        a list representing a matrix. Factor 2

    Returns
    -------
    list
        a list representing the product of the two matrices
    """
    if not _isValidMatrix(matrix1) or not _isValidMatrix(matrix2):
        print("Error: invalid matrix")
        return []

    n_1 = len(matrix1[0])
    n_2 = len(matrix2)
    m = len(matrix1)
    p = len(matrix2[0])

    if n_1 is not n_2:
        print("Error in matmul: matrix1 rows must equal matrix2 columns")
        return []


    multiplied_matrix = [ [] for _ in range(m) ]
    for i in range(m):
        for j in range(p):
            c_i_j = 0
            for n in range(n_1):
                c_i_j += matrix1[i][n] * matrix2[n][j]
            multiplied_matrix[i].append(c_i_j)
    return multiplied_matrix

def _det(matrix):
    """Returns the determinant of a matrix. Only works for 2x2 matrices.

    Parameters
    ----------
    matrix : list
        a list representing a matrix

    Returns
    -------
    number
        the determinant of the matrix
    """
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def invert(matrix):
    """Returns an inverted matrix. Only works for 2x2 matrices.

    Parameters
    ----------
    matrix : list
        a list representing a matrix

    Returns
    -------
    list
        the inverted matrix
    """
    matrix_determinant = _det(matrix)
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    return [[d/matrix_determinant,-b/matrix_determinant],[-c/matrix_determinant, a/matrix_determinant]]

def loadtxt(filename):
    """Loads existing x and y values from a file. Where each pair of values are on a separate line and separated by spaces.

    Parameters
    ----------
    filename : string
        the name of the file to load the values from

    Returns
    -------
    list
        a list of lists where each list contains one pair of x and y values
    """
    data = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            [x, y] = line.split()
            data.append([float(x), float(y)])
    return data
