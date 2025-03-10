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
from pyomo.dae import ContinuousSet, DerivativeVar, Simulator

m = pyo.ConcreteModel()

m.t = ContinuousSet(bounds=(0,1))
m.a = pyo.Var(m.t)
m.b = pyo.Var(m.t)

m.k1 = pyo.Param(initialize=5)
m.k2 = pyo.Param(initialize=1)

m.dadt = DerivativeVar(m.a)
m.dbdt = DerivativeVar(m.b)

m.a[0].fix(1)
m.b[0].fix(0)

def _da(m, t):
    return m.dadt[t] == -m.k1*m.a[t]
m.da_con = pyo.Constraint(m.t, rule=_da)

def _db(m, t):
    return m.dbdt[t] == m.k1*m.a[t] - m.k2*m.b[t]
m.db_con = pyo.Constraint(m.t, rule=_db)

mysim = Simulator(m, package='scipy')
tsim, profiles = mysim.simulate(integrator='vode', numpoints=100)

import matplotlib.pyplot as plt

varorder = mysim.get_variable_order()
for idx, v in enumerate(varorder):
    plt.plot(tsim, profiles[:, idx], label=v)

plt.xlabel('t')
plt.legend(loc='best')
plt.show()

plt.show()
