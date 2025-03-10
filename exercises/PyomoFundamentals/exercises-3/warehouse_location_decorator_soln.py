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


# warehouse_location_decorator_soln.py: Warehouse location
# determination problem using decorator notation
import pyomo.environ as pyo

model = pyo.ConcreteModel(name="(WL)")

W = ['Harlingen', 'Memphis', 'Ashland']
C = ['NYC', 'LA', 'Chicago', 'Houston']
d = {('Harlingen', 'NYC'): 1956, \
     ('Harlingen', 'LA'): 1606, \
     ('Harlingen', 'Chicago'): 1410, \
     ('Harlingen', 'Houston'): 330, \
     ('Memphis', 'NYC'): 1096, \
     ('Memphis', 'LA'): 1792, \
     ('Memphis', 'Chicago'): 531, \
     ('Memphis', 'Houston'): 567, \
     ('Ashland', 'NYC'): 485, \
     ('Ashland', 'LA'): 2322, \
     ('Ashland', 'Chicago'): 324, \
     ('Ashland', 'Houston'): 1236 }
P = 2

model.x = pyo.Var(W, C, bounds=(0,1))
model.y = pyo.Var(W, within=pyo.Binary)

@model.Objective()
def obj(m):
    return sum(d[w,c]*m.x[w,c] for w in W for c in C)

@model.Constraint(C)
def one_per_cust(m, c):
    return sum(m.x[w,c] for w in W) == 1

@model.Constraint(W,C)
def warehouse_active(m, w, c):
    return m.x[w,c] <= m.y[w]

@model.Constraint()
def num_warehouses(m):
    return sum(m.y[w] for w in W) <= P

pyo.SolverFactory('glpk').solve(model)

model.y.pprint()
model.x.pprint()

