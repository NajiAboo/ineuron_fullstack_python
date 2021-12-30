def fun(fn,*params):
    print(params)
    return fn(params)


def display(x):
    print(f"value : {x}")
    
fun(display,5)    