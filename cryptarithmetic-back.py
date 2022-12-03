from csp import *
# from notebook import psource, plot_NQueens

# %matplotlib inline
# Hide warnings in the matplotlib sections

import math
import warnings
warnings.filterwarnings("ignore")

# D A Y S + TOO = SHORT 
# Solve the CSP using backtracking (depth-first search)

# CSP Definition
def days_too_short():
    Vars = 'A D H O R S T Y'.split()
    Conds = 'C1 C2 C3 C4'.split()
    variables = Vars + Conds
    #
    domains = {}
    for var in Vars:
        domains[var] = list(range(0, 10))
    for var in Conds:
        domains[var] = list(range(0, 2))  
    domains['D'] = domains['T'] = list(range(1, 10))
    domains['S'] = [1]
    #
    neighbors = parse_neighbors("""A: D Y S T O H R; D: Y S T O H R; Y: S T O H R;
                                S: T O H R; T: O H R; O: H R; H: R; S: C4""")

    # Not complete: Need to add the neighbors corresponding to the n_ary constraints
    # """C1: S O T Y R; C2: C1 O R Y; C3: C2 A O T; C4: C3 D H""")

    print(domains)
    print(neighbors)

    def dts_constraint(A, a, B, b, recurse=0):
        same = (a == b)
        if A == 'S' and B == 'C4':
            return same
        if recurse == 0:
            return dts_constraint(B, b, A, a, 1)
        if A in Vars and B in Vars:
            return not same

        raise Exception('error')

    return CSP(variables, domains, neighbors, dts_constraint)

# Call solver
dts = days_too_short()
backtracking_search(dts, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)