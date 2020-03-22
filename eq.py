def factorial(fac):
    '''import math
    return math.prod([x for x in range(1,fac+1)])
    return math.factorial(fac)'''
    result=1
    for x in range(1,fac+1):
        result *= x
    return result
def integer(i):
    check=False
    while check==False:
        i=int(i)
        if i<0:
            i=input("Please enter valid number: ")
        else:
            check=True
    print ("done")
def get_eq(eqIn):
    eq = {}
    totalWeight = 0
    from random import randrange
    eqIn = tuple(eqIn.replace(", ", ",").split(","))
    for item in eqIn:
        weight = randrange(1, 5)
        eq[item] = weight
        totalWeight += weight
    print ("Your items: ", *eq, sep="\n")
    return "Nice" if totalWeight / 10 < 1 else "Overwhelmed"

print(get_eq(input("Insert your items, separated by commas: ")))
