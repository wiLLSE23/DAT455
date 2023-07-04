import math
def newtonApprox(r, n):
    x_n = r / 2
    for i in range(n):
        x_n = (x_n + r / x_n) / 2
        print(str(i) + ": " + "Guess is " + str(x_n) + " with error of " + str(math.sqrt(r) - x_n))
    return x_n

print(newtonApprox(2, 10))