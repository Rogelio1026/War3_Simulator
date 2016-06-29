import sys

def cooldown(what_to_reduce,fps):
    if what_to_reduce > 0:
        what_to_reduce -= 1 / fps
        if what_to_reduce < 0.001:
            what_to_reduce = 0
    return what_to_reduce

def str_to_class(str):
    return reduce(getattr, str.split("."), sys.modules[__name__])