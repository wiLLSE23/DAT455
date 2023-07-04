def pyApprox(n):
    pi = 0
    for k in range(n + 1):
        pi += 4 * ((-1) ** k)/(2 * k + 1)
        print("estimate ", str(k), ": ", str(pi))
    return pi

print("py estimate is ", str(pyApprox(10)))