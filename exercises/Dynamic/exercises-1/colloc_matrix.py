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


import numpy

cp = [0, 0.155051, 0.644949, 1]

a = []

print('[')
for i in range(len(cp)):
    ptmp = []
    tmp = 0
    for j in range(len(cp)):
        if j != i:
            row = []
            row.insert(0,1/(cp[i]-cp[j]))
            row.insert(1,-cp[j]/(cp[i]-cp[j]))
            ptmp.insert(tmp,row)
            tmp += 1
    p=[1]
    for j in range(len(cp)-1):
        p = numpy.convolve(p,ptmp[j])
    pder = numpy.polyder(p,1)
    arow = []
    for j in range(len(cp)):
        arow.append(numpy.polyval(pder,cp[j]))
    a.append(arow)
    print(str(arow)+',')
print(']')


                                                              
