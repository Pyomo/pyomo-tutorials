# rosenbrock_script_loop.py: A Pyomo model for the Rosenbrock problem
import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.x = pyo.Var()
model.y = pyo.Var()

def rosenbrock(m):
    return (1.0-m.x)**2 + 100.0*(m.y - m.x**2)**2
model.obj = pyo.Objective(rule=rosenbrock, sense=pyo.minimize)


solver = pyo.SolverFactory('ipopt')

print('x_init, y_init, x_soln, y_soln')
y_init = 5.0
for x_init in range(2, 6):
    model.x = x_init
    model.y = 5.0

    solver.solve(model)

    print("{0:6.2f}  {1:6.2f}  {2:6.2f}  {3:6.2f}".format(x_init, \
            y_init, pyo.value(model.x), pyo.value(model.y)))
    
