A=[1,8,12,16,24,9]
B=[1,24,500,18]
def same_elements(A,B):
    C=[]
    for x in A:
        for i in B:
            if x==i:
                C.append(x)
    return C
print(same_elements(A,B))

