
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:37:05 2020

@author: Christelle
"""

import random

def multip(first_inf, first_sup, second_inf, second_sup):
    a = random.randint(first_inf, first_sup)

    b = random.randint(second_inf, second_sup)

    result = a*b
    
    order_1 = str(a) + " \\times " + str(b) + " = \\textcolor{red}{\\textbf{"+\
           str(result) + "}}"
    
    order_2 = str(b) + " \\times " + str(a) + " = \\textcolor{red}{\\textbf{"+\
           str(result) + "}}"
    
    return random.choice([order_1, order_2])

#    print(a, "*", b, "=", result) 

    
printout = "\\documentclass[a4paper,12pt,twocolumn]{article}\n" +\
"\\usepackage[utf8]{inputenc}\n\\usepackage[francais]{babel}\n\n" +\
"\\usepackage{color}\n\\usepackage{amsmath}\n\n\\usepackage{setspace}\n" +\
"\\onehalfspacing\n\n\\begin{document}\n\n"


levels = ["7P"]*6 + ["8P"]*14


for level in levels:
    
    printout += "\\section*{" + level + "}\n\\begin{spacing}{1.8}\n"+\
        "Nom: ...........................................\n\n" +\
        "Date: ...........................................\n\n" +\
        "Note:\n\\end{spacing}\\begin{enumerate}\n\n"
    
    items = str()
    
    if level == "7P":
        nb_mult_easy = 3
        nb_mult_med  = 6
        nb_mult_diff = 4
        nb_mult_hard = 2
        nb_compl_100 = 2
        nb_compl_50  = 2
        nb_compl_1000= 1
    else:
        nb_mult_easy = 2
        nb_mult_med  = 4
        nb_mult_diff = 5
        nb_mult_hard = 3
        nb_compl_100 = 2
        nb_compl_50  = 2
        nb_compl_1000= 2
        
    for i in range(nb_mult_easy):
        items += "\\item $ "
        items += multip(0, 2, 0, 13) #easy
        items += " $\n"
    
    for i in range(nb_mult_med):
        items += "\\item $ "
        items += multip(3, 5, 3, 13) #medium
        items += " $\n"
    
    for i in range(nb_mult_diff):
        items += "\\item $ "
        items += multip(6, 9, 4, 12) #difficult
        items += " $\n"
    
    for i in range(nb_mult_hard):
        items += "\\item $ "
        items += multip(10, 13, 6, 13) #hard
        items += " $\n"
        
    lines = items.splitlines()
    random.shuffle(lines)
    mix_items = "\n".join(lines)
    
    printout += mix_items
    printout += "\n"
    
    compl_items = str()
    
    for i in range(nb_compl_100):
        c = random.randint(0, 99)
        compl_100 = 100 - c
        compl_items += "\\item $ "
        compl_items += "100 - ....... =" + str(compl_100) +\
            "\\implies \\textcolor{red}{\\textbf{" + str(c) + "}}"
        compl_items += " $\n"
    
    for i in range(nb_compl_50):
        c = random.randint(0, 49)
        compl_50 = 50 - c
        compl_items += "\\item $ "
        compl_items += "50 - ....... =" + str(compl_50) + \
            "\\implies \\textcolor{red}{\\textbf{" + str(c) + "}}"
        compl_items += " $\n"
    
    for i in range(nb_compl_1000):
        c = random.randrange(10, 991, 10)
        compl_1000 = 1000 - c
        compl_items += "\\item $ "
        compl_items += "1000 - ....... =" + str(compl_1000) +\
            "\\implies \\textcolor{red}{\\textbf{" + str(c) + "}}"
        compl_items += " $\n"
    
    printout += compl_items
    
    printout += "\\end{enumerate}\n\n\\newpage"

printout += "\\end{document}"

# print(printout)

with open('generator_display.tex', 'w') as f:
    f.write(printout)
