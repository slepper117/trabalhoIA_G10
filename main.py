from csp import *
# from notebook import psource, plot_NQueens

# %matplotlib inline
# Hide warnings in the matplotlib sections

import math
import warnings
warnings.filterwarnings("ignore")

# CLASS SCHEDULING

def atmost_three(*values):
    return len(values) <= 3

# | Sala 1  | Segunda | Terça | Quarta | Quinta | Sexta |   | AulasLesi | AulasLegi |
# |---------|---------|-------|--------|--------|-------|---|-----------|-----------|
# | 09h:11h | 111     | 121   | 131    | 141    | 151   |   | l11       | l21       |
# | 11h:13h | 112     | 122   | 132    | 142    | 152   |   | l12       | l22       |
# | 14h:16h | 113     | 123   | 133    | 143    | 153   |   | l13       | l23       |
# | 16h:18h | 114     | 124   | 134    | 144    | 154   |   | l14       | l24       |
# |         |         |       |        |        |       |   | l15       | l25       |
# | Sala 2  | Segunda | Terça | Quarta | Quinta | Sexta |   | l16       | l26       |
# | 09h:11h | 211     | 221   | 231    | 241    | 251   |   | l17       | l27       |
# | 11h:13h | 212     | 222   | 232    | 242    | 252   |   | l18       | l28       |
# | 14h:16h | 213     | 223   | 233    | 243    | 253   |   | l19       | l29       |
# | 16h:18h | 214     | 224   | 234    | 244    | 254   |   | l20       | l30       |

# sala1 = list(range(111, 115)) + list(range(121, 125)) + list(range(131, 135)) + list(range(141, 145)) + list(range(151, 155))
# classesLESI = "l11 l12 l13 l14 l15".split()
# classesLEGI = "l21 l22 l23 l24 l25".split()
# variables = classesLESI + classesLEGI

classesLESI = "l11 l12 l13 l14 l15".split()
weekDays = "Monday Tuesday Wednesday Thurday Friday".split()
slotTime = "Tempo1 Tempo2 Tempo3 Tempo4".split()
classRooms = "Room1 Room2".split()

variables = set(classesLESI + weekDays + classRooms + slotTime)

# domain
dominio =  {}
for var in variables:
    dominio[var] = set(range(1, 6))     # list(range(1, 6))
    dominio['l11'] = {1}
    dominio['l12'] = {2}
    dominio['l13'] = {3}
    dominio['l14'] = {4}
    dominio['l15'] = {5}

# constraints
restricoes =   [
    Constraint(classesLESI, all_diff_constraint),
    Constraint(weekDays, all_diff_constraint),
    Constraint(slotTime, all_diff_constraint),
    Constraint(classRooms, all_diff_constraint),
]

# Class scheduling -- Exec 40s
class_scheduling = NaryCSP(dominio, restricoes)

# print variables
print(class_scheduling.variables)

# Result
ans = ac_solver(class_scheduling, arc_heuristic=sat_up)

print(ans)
