import time

def tictoc (func):
    def wrapper():
        t1 =time.time()
        func()
        t2 = time.time()-t1
        print(f'Took {t2}seconds')
    return wrapper


@tictoc
def ffunc():
    i = 0
    for i in range(420000):
        #print(i)
        pass



@tictoc
def wfunc():
    i = 0
    while i < 420000:
        #print(i)
        i=i+1
    
ffunc()

wfunc()