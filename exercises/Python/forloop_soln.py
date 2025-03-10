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


## Write a for loop that prints the entries of the following list, one at a time:
words = ["Wow,", "python", "is", "really", "cool."]

for i in words:
        print(i)

## Write a for loop that computes 2^n only using multiplication by 2
n = 5
val = 2
for i in range(0,n-1):
	val = val*2

print(val)

## Write a for loop that adds 1 to elements in a list and prints their squared value
nums = [0, 3, -2, -1]
for i in nums:
	print((i+1)**2)


