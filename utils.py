import random
class UID:
    _seed = random.getrandbits(32)

    @classmethod
    def uid(cls):
        UID._seed+=1
        return UID._seed
