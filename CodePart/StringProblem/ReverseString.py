def checkPalimdrome(s):
    rev=""
    for i in s:
	    rev = i + rev

    if(s==rev):
	    print("Yes")
    else:
	    print("No")

string = input()
checkPalimdrome(string)