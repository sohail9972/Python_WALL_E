
import numpy as np
#bubble sort where we try to put greqat element to last index


first_array = np.array([20,35,26,45,12,7,6,89,1,2])

def bubble_sort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-i-1):
            if(array[j] > array[j+1]):
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array

print(bubble_sort(first_array))


