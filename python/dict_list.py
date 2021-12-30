def is_iter(var):
    value = False
    if hasattr(var, '__iter__'):
        value = True
    return value

def process(j):
    final_list = []
    print(j)
    if is_iter(j) and type(j) == dict:
        lst = dict_to_list(j)
        final_list.extend(lst)
    elif type(j) == str:
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
        
            
        
def dict_to_list(var):
    final_list = []
    lst = []
   
    for x,j in var.items():
        print(j)
        print(type(j))
        lst.extend(process(j))
    final_list.extend(lst)
            
    return final_list

#a = {'a':[1,2,3,"mak",[23,23,(0,2,3)]], 'b':(1,2,3)}
a1 = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          'a':[1,2,3,"mak",[23,23,(0,2,3)]], 'b':(1,2,3),'x':True,'y':[True,False]}
final1 =  dict_to_list(a1)
print(final1)
