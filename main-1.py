from csp import *
# from notebook import psource, plot_NQueens

# %matplotlib inline
# Hide warnings in the matplotlib sections

import math
import warnings
warnings.filterwarnings("ignore")

# CLASS SCHEDULING

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

#variables = classesLESI + weekDays + classRooms + slotTime

# domain
dominio =  {
    'l11': {1},
    'l12': {2},
    'l13': {3},
    'l14': {4},
    'l15': {5},
    'weekDays': set(range(1, 6)),
    'classRooms': set(range(1, 3))
}


# constraints
restricoes =   [
    Constraint(('l11', 'l12', 'l13', 'l14', 'l15'), all_diff_constraint),
    Constraint(('weekDays', 'classRooms'), all_diff_constraint),
]

# Class scheduling -- Exec 40s
class_scheduling = NaryCSP(dominio, restricoes)

# print variables
print(class_scheduling.variables)

# Result
ans = ac_solver(class_scheduling, arc_heuristic=sat_up)

print(ans)

# Print result
for h in range(1, 6):
    print('Aula', h, end=' ')
    for (var, val) in ans.items():
        if val == h:
            print(var, end=' ')
    print()