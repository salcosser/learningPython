
def tip():
    rawBill = input("Hello, what was the bill?\n")
    rawBill = float(rawBill)

    pTip = input("What percentage do you want to tip?\n")
    pTip = float(pTip) * .01

    tip = pTip * rawBill
    tBill = rawBill + tip

    print("Bill will be " + str(tBill))





tip()