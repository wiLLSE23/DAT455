import matplotlib.pyplot as plt
import sys
from numpy import *

def _poly(a, x):
    """Returns the function value of a polynomial with coefficients a and variable x.

    Parameters
    ----------
    a : list
        a list of coefficients
    x : number
        the variable of the polynomial

    Returns
    -------
    number
        the function value of the polynomial
    """
    y = 0
    for i in range(len(a)):
        y = y + a[i]*x**i
    return y

def _powers(vector, first_power, second_power):
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
    array
        a compact representation of the powers matrix
    """
    if not len(vector):
        print("Error in power: vector is empty")
        return array([])

    if not (first_power >= 0 and second_power >= 0):
        print("Error in power: powers must be larger than 0")
        return array([[]])

    #return matrix
    power_matrix = []
    #vector of all powers
    power_vector = []

    #make sure array contains the vector of all unique powers ranging from first_power to second_power
    for i in range(first_power, second_power+1):
        power_vector.append(i)
      
    #create matrix of powers
    for component in vector:
        power_matrix.append([component**i for i in power_vector])

    return array(power_matrix)

def _non_linear_regression(X, Y, n):
    """Returns the coefficients of a linear regression model.

    Parameters
    ----------
    dataset : list
        a list of lists containing pairs of x and y values
    """

    Xp  = _powers(X,0,n)
    Yp  = _powers(Y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    return a[:,0]

def main():
    """takes a file of of data points and a degree of a polynomial and plots the polynomial that best fits the data points.

    Parameters
    ----------
    arg[1] : str
        the path of data file
    arg[2] : int
        the degree of the polynomial
    """
    data_set = loadtxt(sys.argv[1])
    data = transpose(data_set)
    X = data[0]
    Y = data[1]

    a = _non_linear_regression(X, Y, int(sys.argv[2]))

    x_start = X[0]
    x_end = X[len(X)-1]

    X2 = linspace(x_start,x_end,int((x_end-x_start)/0.2)).tolist()
    Y2 = [ _poly(a, x) for x in X2 ]

    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()

if __name__ == "__main__":
    main()