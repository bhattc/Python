def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def add(a):
    return a + 1
def square(a):
    return a * a
