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


# Your colleague wants to build a classifier that will identify types of bears,
# but is having trouble importing data for her project. Lucikly, you know about
# pandas. No, not the fluffy black and white things, the python data
# manipulation package.

# The file bears-are-bears.csv contains a human-generated categorization of
# several bear specimens obtained by underpaying undergraduate students to
# collect data. Please import the file and display it to the console to verify
# that it matches your expectations.

import pandas

df = pandas.read_csv(--CODE TO IMPORT HERE--)
print(df)

# Your colleague wants to have an alphabetically sorted unique list of all the
# bear types. Generate this from the pandas DataFrame.

print("Sorted bears list:")
print(sorted_bears)

