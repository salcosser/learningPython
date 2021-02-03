

# print("hello world")

############################################



############################################


running = True


while running:
	billValid = False
	tipValid = False
	while not billValid:
		rawBill = input("Hello, what was the bill?\n")
		try:
			float(rawBill)
			billValid = True
		except ValueError:
			print("That was not a valid input. Please give a valid number")
	rawBill = float(rawBill)

	while not tipValid:
		pTip = input("What percentage do you want to tip?\n")
		try:
			float(pTip)
			tipValid = True
		except ValueError:
			print("That was not a valid input. Please give a valid number")
	pTip = float(pTip) * .01

	tBill = (pTip + 1.0) * rawBill

	res = "The total is ${:.2f}."
	print(res.format(tBill))
	restart = input("type \"quit\" to quit the program, or press enter to calculate another bill.\n")
	if restart != "":
		print()
		print()
		print()
		print("Goodbye.")
		print()
		print()
		print()
		running = False