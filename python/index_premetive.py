def index_prem(var):
    if type(var == list or var == tuple or var == set or var == dict):
        for index,value in enumerate(var):
            print(f" index : {index} value : {value}")

index_prem({'a' : 15,'b' : 18,'c' : 20})
            