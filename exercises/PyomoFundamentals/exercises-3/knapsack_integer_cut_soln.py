#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2023-2025
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________


import pyomo.environ as pyo

A = ['hammer', 'wrench', 'screwdriver', 'towel']
b = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}
W_max = 14

model = pyo.ConcreteModel()
model.x = pyo.Var( A, within=pyo.Binary )

def obj_rule(m):
    return sum( b[i]*m.x[i] for i in A )
model.obj = pyo.Objective(rule=obj_rule, sense = pyo.maximize )

def weight_con_rule(m):
    return sum( w[i]*m.x[i] for i in A ) <= W_max
model.weight_con = pyo.Constraint(rule=weight_con_rule)

opt = pyo.SolverFactory('glpk')


# create the ConstraintList to hold the integer cuts
model.int_cuts = pyo.ConstraintList()

# loop 5 times
for l in range(5):
    # solve the problem
    result_obj = opt.solve(model)

    # print the solution
    output_str = 'Obj: ' + str(pyo.value(model.obj))
    for i in A:
        output_str += "  x[%s]: %f" % (str(i), pyo.value(model.x[i]))
    print(output_str)           
    
    # add the integer cut based on the current solution
    cut_expr = 0
    for i in A:
        if pyo.value(model.x[i]) < 0.5:
            cut_expr += model.x[i]
        else:
            cut_expr += (1.0 - model.x[i])
    model.int_cuts.add(cut_expr >= 1)
        

