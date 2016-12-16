import json


def print_dict_as_json(x, n):
    for y in x:
        value = x.get(y)
        if isinstance(value, dict):
            print("\t"*n, y, ":")
            n += 1
            print_dict_as_json(value, n)
            n -= 1
        else:
            print("\t"*n, y, ":", value)
    return
with open("userdata.txt") as f:
    jsonf = json.load(f)
print_dict_as_json(jsonf, 0)
