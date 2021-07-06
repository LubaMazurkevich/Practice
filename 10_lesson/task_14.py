import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        temp=func(*args, **kwargs)
        print(time.time() - start_time)
        return temp
    return wrapper
@timer
def sum_range(start,end):
    summa=0
    if start>end:
        temp=end
        end = start
        start = temp
    for start in range(start,end+1):
        summa+=start
    return summa
print(sum_range(10,2))