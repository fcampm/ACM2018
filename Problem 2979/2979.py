# -*- coding: utf-8 -*-
#Problem 2979 COG Judge
#January 26, 2018
#Fabián Camp Mussa - Github: fcampm.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = (int (x) for x in stdin.read().split())

T = next(nums)
for i in range(T):
    N = next(nums)
    A = []
    for j in range(N):
        A.append(next(nums))
    O = sorted(A)
    c = 0
    for x, y in zip(A, O):
        if x != y:
            c += 1
    print(c)
