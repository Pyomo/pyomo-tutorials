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
