def count_(func):
    def wrapper(*args,**kwargs):
        print("///")
        print(func(*args, **kwargs))
        print("///")
    return wrapper
@count_
def uravnenie(a,b,c):
    D=(b**2)-4*a*c
    if D==0:
        x=-b/2*a
        return x
    elif D>0:
        x1 = (-b + D ** 0.5) / 2*a
        x2 = (-b - D ** 0.5) / 2*a
        return x1,x2
    else :
        return ("нет дейст корней")
uravnenie(2,8,6)




