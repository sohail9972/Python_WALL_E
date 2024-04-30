import numpy as np
str = "Sohail"

def sub_strings(str):
    num=0
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            print(str[i:j])
            num=num+1
    print(num)
sub_strings(str)