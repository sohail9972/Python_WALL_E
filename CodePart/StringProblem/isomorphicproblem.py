import self


def isIsomorphic(s,t) -> bool:

    sStringDict=dict()
    ssignaturelist=[]

    for index ,char in enumerate(s):
        if char not in sStringDict:
            sStringDict[char]=index
        ssignaturelist.append(sStringDict[char])


    tStringDict=dict()
    tStringList=[]
    for index,word in enumerate(t):
        if word not in tStringDict:
            tStringDict[word]=index
        tStringList.append(tStringDict[word])

    return ssignaturelist==tStringList


print(isIsomorphic("egg","foo"))
