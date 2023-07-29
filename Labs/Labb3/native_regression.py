import matplotlib.pyplot as plt
import sys
from matrix import *

def _linear_regression(data_set):
    """Returns the coefficients of a linear regression model.

    Parameters
    ----------
    dataset : list
        a list of lists containing pairs of x and y values
    """
    if not isinstance(data_set[0], list):
        print('Error in linear_regression: invalid dataset')
        return []

    Xp  = powers(data_set[0],0,1)
    Yp  = powers(data_set[1],1,1)
    Xpt = transpose(Xp)

    return matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

def main():
    """takes a file of sentences, one of words and a number
    and prints the fruequency of the x most common words in text
    except those specified in the words file

    Parameters
    ----------
    arg[1] : str
        the path of data file
    """
    data_set = loadtxt(sys.argv[1])
    data = transpose(data_set)
    [[b],[m]] = _linear_regression(data)

    X = data[0]
    Y = data[1]
    Y2 = [ b + m*x for x in X ]

    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    plt.show()

if __name__ == "__main__":
    main()