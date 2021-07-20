spsok=[16,-17,2,78.7,"False",555,12,23,42,"DD",{"True":True}]

def chisla(spsok):
    newlst=[]
    for i in spsok:
        if type(i) == int or type(i) == float:
            newlst.append(i)
    return sorted(newlst)
print(chisla(spsok))