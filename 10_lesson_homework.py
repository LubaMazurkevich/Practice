# with open("domashka.txt","r") as FIN:
#     kol=0
#     sum=0
#     for s in FIN:
#         s = s.split()
#         if int(s[2])<3:
#             print(f"Оценки меньше 3 баллов:{s}")
#         kol+=1
#         sum+=int(s[2])
# print(f"Средний балл :{sum/kol}")
# FIN.close()
#
#
# with open("mylist.txt","r") as fin:
#     kol=0
#     sum=0
#     for s in fin:
#         s = s.split()
#         kol+=1
#         sum+=int(s[2])
# print(f"Средний балл : {sum/kol}")
# fin.close()
#
#
# with open("xyz.txt","r") as Fin:
#     county=0
#     countx=0
#     for s in Fin:
#         s=s.split()
#         for p in s:
#             if p=="x":
#                 countx+=1
#             if p=="y":
#                 county+=1
#     print(f"Количество x:{countx}\nКоличество y:{county}")

from random import randint
#
# def function():
#     spisok1 = []
#     for i in range(10):
#         spisok1.append(randint(1, 25))
#         k=set(spisok1)
#     return spisok1,len(spisok1)-len(k)
# print(f"Список: {function()}-повторяющиеся элементы")

# def createRandomlist():
#     lst = []
#     for i in range(10):
#         lst.append(randint(1, 25))
#     return lst
# def sameelements(resultlst):
#     newlst = []
#     for i in resultlst:
#         if i not in newlst:
#             newlst.append(i)
#     return newlst,len(resultlst)-len(newlst)
# resultlst=createRandomlist()
# print(resultlst)
# result2=sameelements(resultlst)
# print(f"Cписок/Количество повторяющихся элементов: {sameelements(resultlst)}")




#
# def createRandomlist():
#     lst = []
#     for i in range(10):
#         lst.append(randint(1, 25))
#     return lst
# def sameelements(resultlst):
#     newlst = []
#     for i in resultlst:
#         if i not in newlst:
#             newlst.append(i)
#     return newlst
# resultlst=createRandomlist()
# print(resultlst)
# print(sameelements(resultlst))
# dif=len(resultlst)-len((sameelements(resultlst)))
# print(f"Количество повторяющихся элементов: {dif}")
# #
def createRandomlist():
    lst = []
    for i in range(10):
        lst.append(randint(1, 25))
    print(lst)
    return lst
def find_same_elements(lst):
    dct={}
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    # if dct[i]<=1:
    #     i.pop()
    return dct
lstr=createRandomlist()
print(find_same_elements(lstr))




#
# def createRandomlist():
#     lst = []
#     for i in range(10):
#         lst.append(randint(1, 25))
#     print(lst)
#     return lst
# def find_same_elements(lst):
#     dct={}
#     count=1
#     for x in range(len(lst)-1):
#         for j in range(x+1,len(lst)):
#             if lst[x]==lst[j]:
#                 dct[lst[x]]=x
#                 if lst[x] in dct:
#                     count+=1
#                     print(count)
#     return dct,count
# lstr=createRandomlist()
# print(find_same_elements(lstr))


# lst = []
# count0=0
# count1=0
# for i in range(10):
#     lst.append(randint(0, 1))
# for i in lst:
#     if i==0:
#         count0+=1
#     if i==1:
#         count1+=1
# print(lst)
# print(count0,count1)
# dct = {}
# dct[0]=count0
# dct[1]=count1
# print(dct)


# #количество нулей,количество единиц]
# lst=[]
# for i in range(10):
#     lst.append(randint(0, 1))
# dct={}
# for i in lst:
#     try:
#         dct[i]+=1
#     except KeyError:
#         dct[i]=1
# print(lst)
# print(dct)

lst=[]
for i in range(10):
    lst.append(randint(0, 1))
dct={}
for i in lst:
    if i in dct:
       dct[i]+=1
    else:
       dct[i]=1
print(lst)
print(dct)

# def function(spisok):
#     maximum=spisok[0]
#     for x in spisok:
#         if x>maximum:
#             maximum=x
#     return maximum
# spisok=[1,9,10,15]
# print(function(spisok))
#
# function=max
# print(function(spisok))
#
# function=min
# print(function(spisok))





# def season(month):
#     if month==1:
#         return "January"
#     if month==2:
#         return "February"
#     if month==3:
#         return "March"
#     if month==4:
#         return "April"
#     if month==5:
#         return "May"
#     if month==6:
#         return "June"
#     if month==7:
#         return "JuLY"
#     if month==8:
#         return "August"
#     if month==9:
#         return "September"
#     if month==10:
#         return "October"
#     if month == 11:
#         return "November"
#     if month==12:
#         return "December"
# print(season(12))


def season(month):
    dctt = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
            9: "September", 10: "October", 11: "November", 12: "December"}
    return dctt[month]
print(season(month=12))

# def uravnenie(a,b,c):
#     D=(b**2)-4*a*c
#     if D==0:
#         x=-b/2*a
#         return x
#     elif D>0:
#         x1 = (-b + D ** 0.5) / 2*a
#         x2 = (-b - D ** 0.5) / 2*a
#         return x1,x2
#     else :
#         return ("нет дейст корней")
# print(uravnenie(2,8,6))
#
# A=[1,8,12,16,24,9]
# B=[1,24,500,18]
# def same_elements(A,B):
#     C=[]
#     for x in A:
#         for i in B:
#             if x==i:
#                 C.append(x)
#     return C
# print(same_elements(A,B))



def three_args(**kwargs):
    str1 = ""
    for k,v in kwargs.items():
        if v!=None:
            str1 +=k +"="
            str1 += str(v)+" "
    return str1
print(f"Переданы аргументы: {(three_args(var1=1,var2=5,var3=8,var4=None))}")



# def sum_range(start,end):
#     summa=0
#     if start>end:
#         temp=end
#         end = start
#         start = temp
#     for start in range(start,end+1):
#         summa+=start
#     return summa
# print(sum_range(10,2))


# def treugolnik(a,b,c):
#     if a+b>c or a+c>b:
#         return ("Треугольник существует")
#     else:
#         return ("Треугольник не существует")
# print(treugolnik(0,0,0))






# spsok=[16,-17,2,78.7,"False",555,12,23,42,"DD",{"True":True}]
#
# def chisla(spsok):
#     newlst=[]
#     for i in spsok:
#         if type(i) == int or type(i) == float:
#             newlst.append(i)
#     return sorted(newlst)
# print(chisla(spsok))

