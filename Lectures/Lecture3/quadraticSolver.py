import math

def qSolve(a,b,c):
    inner = b**2 - 4*a*c
    if(inner < 0):
        return []
    elif(inner == 0):
        return [-b/(2*a)]
    rInner = math.sqrt(inner)
    return [(-b-rInner)/(2*a), (-b+rInner)/(2*a)]

print(qSolve(1, 0, -50))
    
    