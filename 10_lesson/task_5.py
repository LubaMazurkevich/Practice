def function(spisok):
    maximum=spisok[0]
    for x in spisok:
        if x>maximum:
            maximum=x
    return maximum
spisok=[1,9,10,15]
print(function(spisok))


function=max
print(function(spisok))


function=min
print(function(spisok))
