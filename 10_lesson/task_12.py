def treugolnik(a,b,c):
    if a+b>c or a+c>b:
        return ("Треугольник существует")
    else:
        return ("Треугольник не существует")
print(treugolnik(0,0,0))