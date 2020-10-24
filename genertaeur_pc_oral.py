# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:37:05 2020

@author: Christelle
"""

import random

def multip(first_inf, first_sup, second_inf, second_sup):
    a = random.randint(first_inf, first_sup)

    b = random.randint(second_inf,second_sup)

    result = a*b

    print(a, "*", b, "=", result)
    
    
printout = "\\documentclass[a4paper,12pt,twocolumn]{article}\n" +\
"\\usepackage[utf8]{inputenc}\n\\usepackage[francais]{babel}\n\n" +\
"\\usepackage{color}\n\n\\begin{document}\n"
    
multip(0,2,0,13) #easy

multip(3,5,3,13) #medium

multip(6,9,4,12) #difficult

multip(10,13,6,13) #hard

c = random.randint(0,99)

compl_100 = 100 - c

print("100 - .... =", compl_100, "=>", c)

compl_50 = 50

print(random.randrange(10,991,10))

compl_1000 = 1000

print(printout)
