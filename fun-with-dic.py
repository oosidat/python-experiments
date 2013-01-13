new_dict = {"20369106" : { "A3" : 98.0 },"20100501" : { "A3" : 94.0 },\
            "19991007" : { "midterm" : "DNW", "A3" : "DNW" },\
            "19900101" : { "A4" : 13.0, "A3" : 95.0 }}

def func(dictx, strx):
    listx = dictx.keys()
    L = []
    for item in listx:
        if dictx[item].has_key(strx):
            L.append(dictx[item][strx])
    L = (filter(lambda x: type(x) == float,L))
    L.sort()
    return L

print func(new_dict, "A3")