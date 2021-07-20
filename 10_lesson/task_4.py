from random import randint

def createRandomlist():
    lst = []
    for i in range(10):
        lst.append(randint(1, 25))
    return lst
def sameelements(resultlst):
    newlst = []
    for i in resultlst:
        if i not in newlst:
            newlst.append(i)
    return newlst
resultlst=createRandomlist()
print(resultlst)
print(sameelements(resultlst))
dif=len(resultlst)-len((sameelements(resultlst)))
print(f"Количество повторяющихся элементов: {dif}")