import json
def print_as_json(x):
    for y in x:
        value = x.get(y)
        if isinstance(value,dict):
            print_as_json(value)
        else:
            print(y,":",value)
    return
with open("userdata.txt") as f:
    jsonf=json.load(f)
    #y=f.read()
print_as_json(jsonf)