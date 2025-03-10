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
model.item_benefit = # TODO: DEFINE THE PYOMO PARAM HERE

def obj_rule(m):
    return sum( m.item_benefit[i]*m.x[i] for i in A )
model.obj = pyo.Objective(rule=obj_rule, sense = pyo.maximize )

def weight_rule(m):
    return sum( w[i]*m.x[i] for i in A ) <= W_max
model.weight = pyo.Constraint(rule=weight_rule)

opt = pyo.SolverFactory('glpk')

for wrench_benefit in range(1,11):
    model.item_benefit['wrench'] = wrench_benefit
    result_obj = opt.solve(model)

    # TODO: PRINT THE BENEFIT OF THE WRENCH FOR EACH ITERATION IN THE LOOP

