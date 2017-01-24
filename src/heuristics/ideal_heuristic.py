

def get_ideal(arr):
    size = len(arr)
    lookup = {}
    _sorted = sorted(arr)

    for i,x in enumerate(_sorted):
        lookup[x] = i/size

    def h(x):
        return lookup[x]

    return h
