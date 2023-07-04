def pythTrios(x):
    for c in range(x):
        for b in range(1, c):
            for a in range(1, b):
                if(a ** 2 + b ** 2 == c ** 2):
                    print(str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2")
pythTrios(100)