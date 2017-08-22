import random
class UID:
    _seed = random.getrandbits(32)

    @classmethod
    def uid(cls):
        UID._seed+=1
        return UID._seed

def reduceTuple(tpl):
    x = tpl[0]
    y = tpl[1]
    if x > 0: x = 1
    elif x < 0: x = -1
    if y > 0: y = 1
    elif y < 0: y = -1

    return (int(x),int(y))
