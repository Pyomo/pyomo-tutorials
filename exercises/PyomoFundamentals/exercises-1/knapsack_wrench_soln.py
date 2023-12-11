import pyomo.environ as pyo

A = ['hammer', 'wrench', 'screwdriver', 'towel']
b = {'hammer':8, 'wrench':8, 'screwdriver':6, 'towel':11}
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}
W_max = 14

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
