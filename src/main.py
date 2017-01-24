from __future__ import print_function
import numpy as np
import timeit
import copy
import matplotlib.pyplot as plt

from heuristic_sort import heuristic_sort_generator

xrange = range

#Section quicksort
def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)


def time_for_algo(sorter,dataset):
    ds = copy.deepcopy(dataset)
    return [timeit.Timer(lambda: sorter(x)).timeit(number=50) for x in ds]

NUM_DATA_SETS = 3
if __name__ == "__main__":
    print("\nEntering main function.  Generating Data.")
    d_sets = [np.random.normal(0,50,x**2) for x in range(1,NUM_DATA_SETS)]

    print("Created %d Datasets\n" % (NUM_DATA_SETS))
    print("Measuring time for O(n Log(n)) sort.")
    nlogn_times = time_for_algo(quicksort,d_sets)
    print("O(n Log(n)) times measued.")
    print("Timing Heuristic Sort.")
    hsort_times = time_for_algo(heuristic_sort_generator(lambda x: .5),d_sets)
    print("Finished Timing Heuristic Sort")

    plt.plot([len(x) for x in d_sets],nlogn_times)


    plt.show()
