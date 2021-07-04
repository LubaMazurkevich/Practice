with open("mylist.txt","r") as fin:
    kol=0
    sum=0
    for s in fin:
        s = s.split()
        kol+=1
        sum+=int(s[2])
print(f"Средний балл : {sum/kol}")
fin.close()

