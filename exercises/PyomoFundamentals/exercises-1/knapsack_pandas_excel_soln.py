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


import pandas as pd
import pyomo.environ as pyo

df_items = pd.read_excel('knapsack_data.xlsx', sheet_name='data', header=0, index_col=0)
W_max = 14

A = df_items.index.tolist()
b = df_items['Benefit'].to_dict()
w = df_items['Weight'].to_dict()

model = pyo.ConcreteModel()
model.x = pyo.Var( A, within=pyo.Binary )

model.obj = pyo.Objective(
    expr = sum( b[i]*model.x[i] for i in A ), 
    sense = pyo.maximize )

model.weight_con = pyo.Constraint(
    expr = sum( w[i]*model.x[i] for i in A ) <= W_max )

opt = pyo.SolverFactory('glpk')
opt_success = opt.solve(model)

total_weight = sum( w[i]*pyo.value(model.x[i]) for i in A )
print('Total Weight:', total_weight)
print('Total Benefit:', pyo.value(model.obj))

print('%12s %12s' % ('Item', 'Selected'))
print('=========================')
for i in A:
    acquired = 'No'
    if pyo.value(model.x[i]) >= 0.5:
        acquired = 'Yes'
    print('%12s %12s' % (i, acquired))
print('-------------------------')
