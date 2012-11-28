# coding:utf-8

class Chap9:
    cache = []
    def __init__(self, n):
        for i in xrange(n+1):
            Chap9.cache.append(-1) 

    def Question1(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            q1 = Chap9(n)
            return q1.Question1(n-1) + q1.Question1(n-2) + q1.Question1(n-3)

    def Question1_rev(self, n):
        if self.cache[n] != -1:
            return self.cache[n]
        elif n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            q1 = Chap9(n)
            self.cache[n] = q1.Question1_rev(n-1) + q1.Question1_rev(n-2) + q1.Question1_rev(n-3)
            return self.cache[n]
