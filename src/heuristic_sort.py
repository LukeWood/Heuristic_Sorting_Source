def ins_sort(k):
    for i in range(1,len(k)):    #since we want to swap an item with previous one, we start from 1
        j = i                    #bcoz reducing i directly will mess our for loop, so we reduce its copy j instead
        while j > 0 and k[j] < k[j-1]: #j>0 bcoz no point going till k[0] since there is no value to its left to be swapped
            k[j], k[j-1] = k[j-1], k[j] #syntactic sugar: swap the items, if right one is smaller.
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
    return k

def heuristic_sort_generator(heuristic):

    def sorter(arr):
        size = len(arr)
        slots_taken = [False] * size
        _sorted = [None] * size

        for x in arr:

            val = int(heuristic(x) * size)

            #Base case
            if(not slots_taken[val]):
                slots_taken[val] = True
                _sorted[val] = x
                #TODO:: Modify the "get next position method"
                continue
            else:
                #TODO::Use the get next position method w/ lookup table
                ival = val
                while(val < size):
                    if(not slots_taken[val]):
                        slots_taken[val] = True
                        _sorted[val] = x
                        break
                    val+=1

                if(val == size):
                    val = ival-1
                    while(val >= 0):
                        if(not slots_taken[val]):
                            slots_taken[val] = True
                            _sorted[val] = x
                            break
                        val-=1
        return ins_sort(_sorted)

    return sorter
