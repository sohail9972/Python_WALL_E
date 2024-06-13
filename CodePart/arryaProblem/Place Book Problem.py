def placeBooks(arr, k):
    if k==0:
        return True

    bookCount=0

    for i in range(len(arr)):
        isleft=(i==0) or (arr[i-1]==0)
        isright = (i==len(arr)-1) or (arr[i+1]==0)


        if(arr[i]==0 and isleft and isright):
            arr[i]=1
            bookCount +=1
            if(bookCount==k):
                return True

    return False
