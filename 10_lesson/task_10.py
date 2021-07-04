def three_args(**kwargs):
    str1 = ""
    for k,v in kwargs.items():
        if v!=None:
            str1 +=k +"="
            str1 += str(v)+" "
    return str1
print(f"Переданы аргументы: {(three_args(var1=1,var2=5,var3=8,var4=None))}")


