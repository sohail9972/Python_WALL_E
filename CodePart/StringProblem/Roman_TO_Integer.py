def romanToInt(s):
    dictonary = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    result = 0
    for i in range(len(s)):
        if i+1 < len(s) and dictonary[s[i]] < dictonary[s[i+1]]:
            result -= dictonary[s[i]]
        else:
            result +=dictonary[s[i]]
    return result





print(romanToInt("XXCML"))
