with open("domashka.txt", "r") as FIN:
    kol=0
    sum=0
    for s in FIN:
        s = s.split()
        if int(s[2])<3:
            print(f"Оценки меньше 3 баллов:{s}")
        kol+=1
        sum+=int(s[2])
print(f"Средний балл :{sum/kol}")
FIN.close()

