from random import randint


class LinearRec:
    mod = 0
    x_arr = []
    a_arr = []
    n = 0
    c = 0

    def get_new_c(self):
        pass


class Fibonacci:
    r = 0
    s = 0
    t = 0
    x_arr = []

    def __init__(self, r=None, s=None, x_arr=None):
        if r is None:
            self.r = randint(0, 128)
        if s is None:
            self.s = randint(0, 128)
        if x_arr is None:
            self.x_arr = []
            for i in range(r):
                self.x_arr.append(randint(0, 128))
        self.t = r

    def get_new_x(self):
        res = self.x_arr[self.t - self.r] ^ self.x_arr[self.t - self.s]
        self.x_arr.append(res)
        self.t += 1
        return
