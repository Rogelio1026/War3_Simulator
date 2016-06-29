def cooldown(what_to_reduce,fps):
    if what_to_reduce > 0:
        what_to_reduce -= 1 / fps
        if what_to_reduce < 0.001:
            what_to_reduce = 0
    return what_to_reduce

