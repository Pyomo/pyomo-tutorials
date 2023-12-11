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
opt_success = opt.solve(model)

model.pprint()

