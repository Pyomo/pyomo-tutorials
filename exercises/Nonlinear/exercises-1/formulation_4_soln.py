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

model = pyo.ConcreteModel()

model.x = pyo.Var(initialize=5.0)
model.y = pyo.Var(initialize=5.0, bounds=(0,None))

def obj_rule(m):
    return (m.x-1.01)**2 + m.y**2
model.obj = pyo.Objective(rule=obj_rule)

def con_rule(m):
    return (m.x - 1.0) / m.y == 1.0
model.con = pyo.Constraint(rule=con_rule)

solver = pyo.SolverFactory('ipopt')
solver.solve(model, tee=True)

print(pyo.value(model.x))
print(pyo.value(model.y))
