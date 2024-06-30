
def addBinary(a: str, b: str) -> str:
    x=int(a,2)
    print(x)
    y=int(b,2)
    print(y)
    result= x + y

    print(bin(result))

addBinary("100","1")
