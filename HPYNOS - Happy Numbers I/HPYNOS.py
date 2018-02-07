# -*- coding: utf-8 -*-
#Problem HPYNOS Spoj
#January 26, 2018
#Fabián Camp Mussa - Github: fcampm.

from __future__ import print_function
from __future__ import division

entrada = input()
n = len(entrada)

def simple(entrada):
    cad = str(entrada)
    suma = 0
    for c in cad:
        suma += int(c) ** 2
    return suma

def main():
    res = int(entrada)
    counter = 0
    while(res != 1):
        res = simple(res)
        counter += 1

    print (counter)
main()
