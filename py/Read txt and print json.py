import json


def print_as_json(x,n):
    for y in x:
        value = x.get(y)
        if isinstance(value, dict):
            n = n+1
            print_as_json(value,n)
        else:
            print("\t"*n, y, ":", value)
    return
with open("userdata.txt") as f:
    jsonf = json.load(f)
print_as_json(jsonf,0)
