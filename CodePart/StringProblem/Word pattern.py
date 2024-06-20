def wordPattern(self, pattern: str, s: str) -> bool:

    patterndict= dict()
    signaturepatternlist=[]

    for index,char in enumerate(pattern):
        if char not in patterndict:
            patterndict[char]=index
        signaturepatternlist.append(patterndict[char])

    # creating  empty dictonary and signature list
    # singnature list will store the 1 0 patern of the Words and Characters

    wordofSdict = dict()
    wordofSinList=[]

    for index,word in enumerate(s.split(" ")):
        if word not in wordofSdict:
            wordofSdict[word]=index
        wordofSinList.append(wordofSdict[word])

    return wordofSinList==signaturepatternlist

