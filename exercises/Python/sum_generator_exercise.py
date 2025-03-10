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


# There are 100 toucans at the pet store, but your parents will only allow you
# to bring home one. The constraint for this looks like \sum_{i=1}^{100} x_i = 1.
# Express this constraint in Pyomo:

# m = ConcreteModel()
# m.toucans = RangeSet(100)
# m.x = Var(m.toucans, domain=Binary,
#           doc="Binary variable denoting selection of a toucan.")
# m.pick_one_toucan = Constraint(expr=sum(--FILL THIS IN--) == 1)

# Answer:

m = ConcreteModel()
m.toucans = RangeSet(100)
m.x = Var(m.toucans, domain=Binary,
          doc="Binary variable denoting selection of a toucan.")
m.pick_one_toucan = Constraint(expr=sum(m.x[i] for i in m.toucans) == 1)
