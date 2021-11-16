import time


def timeit(func):
    def wrapper(*arg , **kwargs):
        starttime=time.time()
        value=func(*arg , **kwargs)
        endtime=time.time()
        print(f"runing : {func.__name__} take time : {endtime - starttime}")
        return value
    return wrapper


@timeit
def view1(request):
    for i in range(0,1000):
        pass
    
    
@timeit
def view2(request):
    for i in range(0,1000000):
        pass
    
    
    
@timeit
def view3(request):
    for i in range(0,50000000):
        pass
    
        
view1(1)

view2(1) 

view3(1) 
      