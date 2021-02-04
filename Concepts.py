


#data types
x = 3
y = "Hello"
b = True
n = 1.213


#printing
print("Hello, World")

#getting input
inp = input("What's your favorite food?")
print("Oh, I love " inp "!")



#varable assignment
this = 5
that = 4



#conditions
if this > that:
    print("This is bigger than that!")
elif that > this:
    print("That is bigger than this!")
else:
    print("Niether is bigger!")


thing = False

if not thing:       #looks like giberish
    print("Thing is false")



#loops

for i in range(5):
    print("Hello #" + i)


num = 10
while num > 6:
    num-=1
    print("now num is " + num)

#functions

def func():
    print("Function activated.")

def addSix(n):
    return n + 6