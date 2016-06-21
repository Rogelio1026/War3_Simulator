def compare_doubles(double1, double2):
    if abs(double1 - double2) <= 0.001:
        return True

def cooldown(what_to_reduce,fps):
    if what_to_reduce > 0:
        what_to_reduce -= 1 / fps
        if what_to_reduce < 0.001:
            what_to_reduce = 0
    return what_to_reduce