import time

class RandomInt():
    def __init__(self):
        self._state = int(time.time() * 1000)

    def next(self, n):

        self._state *= 48271
        self._state = self._state % (2**32)
        state_n = self._state % n
        return state_n
