def search3(L, e):
    print("List L: " + str(L))
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
search3([], 4)
