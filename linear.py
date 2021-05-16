from random import randint
import argparse
from time import time
'''
генератор (1.4.1) ‒ (1.4.2); генератор Фибоначчи F(r, s, ⊕)

'''


class LinearRec:
    x_arr = []
    a_arr = []
    n = 0
    c = 0
    modulus = 0
    t = 0

    def __init__(self, mod=0, a_arr_0=None, x_arr_0=[], c_0=0):
        assert len(x_arr_0) >= len(a_arr_0), 'len of x must be greater or equal a'
        if mod == 0:
            mod = randint(0, 1024)
        if a_arr_0 is None:
            self.a_arr = []
            for i in range(5):
                self.a_arr.append(randint(0, mod))
        else:
            self.a_arr = a_arr_0
        if x_arr_0 is None:
            self.x_arr = []
            for i in range(5):
                self.x_arr.append(randint(0, mod))
        else:
            self.x_arr = x_arr_0
        self.n = len(self.a_arr)
        if c_0 == 0:
            self.c = randint(0, 1024)
        else:
            self.c = c_0
        self.modulus = mod
        t = len(self.x_arr)
        print('Linear instance created! a = {}, x = {}, c = {}, modulus = {}'.format(self.a_arr, self.x_arr, self.c, self.modulus))

    def get_new_c(self, sum):
        res = int((sum + self.c) / self.modulus)
        #print('new c is {}'.format(res))
        self.c = res
        return res

    def get_new_x(self):
        sum_x = 0
        for i in range(self.n):
            sum_x += self.a_arr[self.n - 1 - i] * self.x_arr[-1 - i]
        #print('new sum_x = {}'.format(sum_x))
        sum_x = (sum_x + self.get_new_c(sum_x)) % self.modulus
        self.x_arr.append(sum_x)
        return sum_x


def args():
    parser = argparse.ArgumentParser(description='Linear lab')
    parser.add_argument('-m', type=int, help='0 for file, 1 for args, 2 for rand', default=1)
    parser.add_argument('-a', type=int, nargs='+', default=None)
    parser.add_argument('-x', type=int, nargs='+', default=None)
    parser.add_argument('-c', type=int, default=0)
    parser.add_argument('--mod', type=int, default=0)
    parser.add_argument('-f', '--file', type=str, default='')
    parser.add_argument('-o', type=int, default=0)
    args = parser.parse_args()
    return args.m, args.a, args.x, args.c, args.mod, args.o, args.file


def main():
    mode, a, x, c, mod, cnt, file_str  = args()
    #print(x)
    if mode == 0:
        with open(file_str) as f:
            text = f.readlines()
        print(text)
        a = LinearRec()
    else:
        a = LinearRec(mod, a, x, c)
    start = time()
    with open('res_lin.txt', 'w') as f:
        for i in range(cnt):
            res = a.get_new_x()
            #print(res)
            f.write(str(res) + '\n')
    timer = time() - start
    print("For {} samples {} seconds. {} samples per second".format(cnt, timer, cnt / timer))


if __name__ == '__main__':
    main()




