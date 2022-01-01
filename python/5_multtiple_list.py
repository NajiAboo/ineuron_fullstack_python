def is_iter(var):
    value = False
    if hasattr(var, '__iter__'):
        value = True
    return value

def process(j):
    final_list = []
    
    if type(j) == str:
        final_list.append(j)  
    elif is_iter(j) and type(j) != dict:
        lst = iter_to_list(j)
        final_list.extend(lst)
    else:
        final_list.append(j)
        
    return final_list
    

def iter_to_list(var):
    final_list = []
    lst = []
    for j in var:
        lst.extend(process(j))
    final_list.extend(lst)
    return final_list

def multi_list_con(*inp):
    """concatinate the input 
    input should be multiple lists

    Returns:
        [type]: [description]
    """
    final_list = []
    for l in inp:
        if type(l)==list:
            lst = iter_to_list(l)
            final_list.extend(lst)
        else:
            print("onlyt list is allowed")
    print(final_list)
    return final_list



multi_list_con([1,2],[3,4],[5,6,7,8,"naji"])