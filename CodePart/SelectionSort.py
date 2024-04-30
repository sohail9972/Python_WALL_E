import numpy as np

unsorted_array = np.array([20,35,26,45,12,7,6,89,1,2])


def getMax(array, first, j):
    maxi = first
    for i in range(first,j+1):
        if(array[maxi]<array[i]):
            maxi=i
    return maxi


def swaping(array, iammax, second):
        temp = array[iammax]
        array[iammax] = array[second]
        array[second]=temp
def selection_srt(array):
    for first in range(0,len(array)):
        last = len(array)-first-1
        iammax = getMax(array,0,last)
        print(iammax)
        swaping(array,iammax,last)
    return array



print(selection_srt(unsorted_array))