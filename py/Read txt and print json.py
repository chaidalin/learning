import json


# 从文本文档读取连续的json格式字符串转换成字典再逐个数据打印到屏幕，把dict类型的数据再按层级缩进再展开。
def print_dict_as_json(x, n):
    for y in x:
        value = x.get(y)
        if isinstance(value, dict):
            print("\t" * n, y, ":")
            n += 1
            print_dict_as_json(value, n)
            n -= 1
        else:
            print("\t" * n, y, ":", value)
    return
with open("userdata.txt") as f:
    jsonf = json.load(f)
print_dict_as_json(jsonf, 0)
