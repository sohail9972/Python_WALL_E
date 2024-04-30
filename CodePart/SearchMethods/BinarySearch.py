import numpy as np

searchSpace = np.array([1,2,6,7,12,20,26,35,45,89])
target = 45;


def binsearch(array,tar):
    start = 0
    end=len(array)-1
    while(start<=end):
        mid = start + (end-start)//2
        if(tar<array[mid]):
            end=mid-1
        elif(tar>array[mid]):
            start=mid +1
        else:
            return mid



print(binsearch(searchSpace,target))