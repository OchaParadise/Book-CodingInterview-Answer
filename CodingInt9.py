# coding:utf-8

import sys
from Class.Class9 import Chap9

def chap9_q1(n):
    q1 = Chap9(n)
    print q1.Question1_rev(n)

if __name__ == '__main__':
    num = int(sys.argv[1])
    chap9_q1(num)
