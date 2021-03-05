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

    def __init__(self, r=None, s=None, x_arr=None, max_num=128):
        if r is None:
           r = randint(0, max_num)
        self.r = r
        if s is None:
            s = randint(0, max_num)
            while s > r:
                s = randint(0, max_num)
        self.s = s
        if x_arr is None:
            x_arr = []
            for i in range(r):
                x_arr.append(randint(0, max_num))
        self.x_arr = x_arr
        assert r == len(self.x_arr), 'r is not equal to arr len'
        self.t = r - 1
        print('Fibonacci instance created! r = {}, s = {}, x_arr = {}'.format(self.r, self.s, self.x_arr))

    def get_new_x(self):
        res = self.x_arr[self.t - self.r] ^ self.x_arr[self.t - self.s]
        self.x_arr.append(res)
        self.t += 1
        return res

    def write_x_res_to_file(self, num, file_name):
        with open(file_name, "w") as f:
            for i in range(num):
                res = self.get_new_x()
                f.write('{}\n'.format(res))






