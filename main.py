


def tip():
    rawBill = input("Hello, what was the bill?\n")
    rawBill = float(rawBill)

    pTip = input("What percentage do you want to tip?\n")
    pTip = float(pTip) * .01

    tip = pTip * rawBill
    tBill = rawBill + tip

    print("Bill will be " + str(tBill))

def fb():

    for i in  range(100):
        
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))



def main():
    fb()
    tip()





main()