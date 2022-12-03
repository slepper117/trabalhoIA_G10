from csp import *
# from notebook import psource, plot_NQueens

# %matplotlib inline
# Hide warnings in the matplotlib sections

import math
import warnings
warnings.filterwarnings("ignore")

# CLASS SCHEDULING

# Schedules


# domain
dominio =  {
            
            }

# constraints
restricoes =   [
                # Classes

                # Profs

                ]

# Class scheduling -- Exec 40s
class_scheduling = NaryCSP(dominio, restricoes)

# print variables
print(class_scheduling.variables)

# Result
ac_solver(class_scheduling, arc_heuristic=sat_up)