# -*- coding: UTF-8 -*-
# 约瑟夫环
def f(N, K):
    l = range(0, N)
    B = 0   # index
    for i in range(0, N - 1):   # kill N-1 round person
        B = (K + B) % len(l)    # 首尾相接
        print "ID:" + str(l[B]) + 'died'
        l.remove(l[B])
    print'last:' + str(l[0])
    return l

l = f(15,20)
print l