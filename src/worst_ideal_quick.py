from __future__ import print_function
import numpy as np
import timeit
import copy
import matplotlib.pyplot as plt

from src.heuristic_sort import heuristic_sort_generator
from src.heuristics.ideal_heuristic import get_ideal

#Global Constants
NUM_DATA_SETS = 1000
OUTPUT_FILE = "img/Proof_Of_Concept.png"

#For Compatibility w/ old versions of numpy
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
    return [timeit.Timer(lambda: sorter(copy.deepcopy(x))).timeit(number=100) for x in dataset]

def time_ideal_hsort(dataset):
    results = []
    for x in dataset:
        sorter = heuristic_sort_generator(get_ideal(x))
        results.append(timeit.Timer(lambda: sorter(copy.deepcopy(x))).timeit(number=100))
    return results

def worst_quick_ideal_main():
    global OUTPUT_FILE
    global NUM_DATA_SETS

    d_sets = [np.random.normal(0,50,x) for x in np.arange(50,NUM_DATA_SETS,50)]

    nlogn_times = time_for_algo(quicksort,d_sets)

    worst_hsort_times = time_for_algo(heuristic_sort_generator(lambda x: .5),d_sets)

    ideal_hsort_times =  time_ideal_hsort(d_sets)

    plt.plot([len(x) for x in d_sets],nlogn_times, label="Quicksort")
    plt.plot([len(x) for x in d_sets],ideal_hsort_times, label="Best Case Heuristic")
    plt.plot([len(x) for x in d_sets],worst_hsort_times, label="Worst Case Heuristic")
    plt.ylabel('Time (ms)')
    plt.xlabel("Number of Unsorted Elements")
    plt.legend()
    while(True):
        try:
            plt.savefig(OUTPUT_FILE)
            break;
        except:
            print("Could not save to %s" % (OUTPUT_FILE))
            OUTPUT_FILE = input("Enter new File Name:")

    OUTPUT_FILE = "img/Ideal_vs_Quicksort.png"

    plt.clf()
    plt.plot([len(x) for x in d_sets],nlogn_times, label="Quicksort")
    plt.plot([len(x) for x in d_sets],ideal_hsort_times, label="Best Case Heuristic")
    plt.ylabel('Time (ms)')
    plt.xlabel("Number of Unsorted Elements")
    plt.legend()
    while(True):
        try:
            plt.savefig(OUTPUT_FILE)
            break;
        except:
            print("Could not save to %s" % (OUTPUT_FILE))
            OUTPUT_FILE = input("Enter new File Name:")

    print("Figure for Best Case and Quicksort saved to %s." % (OUTPUT_FILE))

if __name__ == "__main__":
    worst_quick_ideal_main()
