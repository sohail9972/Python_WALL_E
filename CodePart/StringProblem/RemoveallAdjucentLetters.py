def adjust(s):
    stack=[]
    for letter in s:
        if(len(stack)==0):
            return True
        else:
            if(stack[-1]!=letter):
                stack.append(letter)
            else:
                stack.pop(letter)
    return "".join(letter)
