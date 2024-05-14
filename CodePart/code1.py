import numpy as np

first_arr= np.array([2,3,45,1,21,41,28,23,75,12])



def bibsort(arr):

    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                temp= arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    # print(arr)
    # print(arr[i])
    return arr[0]




print(bibsort(first_arr))
