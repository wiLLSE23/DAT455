def fakultet(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

for i in range(10):
    print("Fakulteten av " + str(i), fakultet(i))