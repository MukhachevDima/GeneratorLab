from random import randint
import argparse
from time import time
'''
генератор (1.4.1) ‒ (1.4.2); генератор Фибоначчи F(r, s, ⊕)

'''


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
        self.t = r
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

def args():
    parser = argparse.ArgumentParser(description='Fibonacci lab')
    parser.add_argument('-m', type=int, help='0 for file, 1 for args, 2 for rand', default=1)
    parser.add_argument('-r', type=int, help='r', default=None)
    parser.add_argument('-s', type=int, help='s', default=None)
    parser.add_argument('-f', '--file', type=str, default='')
    parser.add_argument('-o', type=int, default=0)
    parser.add_argument('-x', type=int, nargs='+', default=0)
    args = parser.parse_args()
    return args.m, args.r, args.s, args.file, args.o, args.x

def check_args(mode, r, s, string):
    if mode == 0 and string == '':
        print('if you want to read from file you need to type it!')
        return -1
    if mode == 1 and (r is None or s is None):
        print('if you want to read from args you need to type it!')
        return -1
    return mode

def main():
    mode, r, s, file_str, cnt, x = args()
    check_res = check_args(mode, r, s, file_str)
    if check_res == 0:
        with open(file_str) as f:
            text = f.readlines()
        print(text)
        a = Fibonacci()
    elif  check_res == 1:
        if type(x) == list:
            a = Fibonacci(r, s, x)
        else:
            a = Fibonacci(r, s)
    elif check_res == 2:
        if type(x) == list:
            a = Fibonacci(x_arr=x)
        else:
            a = Fibonacci()
    else:
        print('wrong format')
        return
    start = time()
    with open('res_fib.txt', 'w') as f:
        for i in range(cnt):
            res = a.get_new_x()
            #print(res)
            f.write(str(res) + '\n')
    timer = time() - start
    print("For {} samples {} seconds. {} samples per second".format(cnt, timer, cnt/timer))
if __name__ == '__main__':
    main()




