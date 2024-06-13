def reverseByWord(s, left, right):
    while left <= right:
        s[left],s[right] = s[right],s[left]
        left +=1
        right -=1


def reverse(s):
    s=list(s)
    n=len(s)
    beg=0
    for i in range(n):
        if s[i]==" ":
            reverseByWord(s,beg,i-1)
            beg = i+1

    reverseByWord(s,beg,n-1)
    reverseByWord(s,0,n-1)
    s="".join(s)
    print(s)


reverse("Hello I am Shreyashish Sengupta")