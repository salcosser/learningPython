n = input("What number?")
n = int(n)

def fact(x):
    if x == 1:
        return 1
    else:
        return(x * fact(x-1))

print(str(fact(n)))
