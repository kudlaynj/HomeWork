from pprint import pprint


def introspection_info(obj):
    obj = ""
    print(type(obj))
    pprint(dir(obj))


introspection_info(obj="Hello!")
pprint(dir())