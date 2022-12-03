from csp import *
# from notebook import psource, plot_NQueens

# %matplotlib inline
# Hide warnings in the matplotlib sections

import math
import warnings
warnings.filterwarnings("ignore")

# Solve Zebra using backtracking search

solve_zebra(algorithm=backtracking_search, 
            select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)