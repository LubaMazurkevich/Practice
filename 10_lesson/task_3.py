with open("xyz.txt","r") as Fin:
    county=0
    countx=0
    for s in Fin:
        s=s.split()
        for p in s:
            if p=="x":
                countx+=1
            if p=="y":
                county+=1
    print(f"Количество x:{countx}\nКоличество y:{county}")