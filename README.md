# Pyomo Tutorials

This repository hosts a modern, updated set of Pyomo tutorials to reflect
the most recent major version's features and offerings. These tutorials are
intended for those new to Pyomo but who have a reasonable understanding of
optimization modeling.

## Pyomo Overview

Pyomo is a Python-based open-source software package that supports a
diverse set of optimization capabilities for formulating and analyzing
optimization models. Pyomo can be used to define symbolic problems,
create concrete problem instances, and solve these instances with
standard solvers. Pyomo supports a wide range of problem types,
including:

 -  Linear programming
 -  Quadratic programming
 -  Nonlinear programming
 -  Mixed-integer linear programming
 -  Mixed-integer quadratic programming
 -  Mixed-integer nonlinear programming
 -  Mixed-integer stochastic programming
 -  Generalized disjunctive programming
 -  Differential algebraic equations
 -  Mathematical programming with equilibrium constraints
 -  Constraint programming

Pyomo supports analysis and scripting within a full-featured programming
language. Further, Pyomo has also proven an effective framework for
developing high-level optimization and analysis tools.  For example, the
[`mpi-sppy`](https://github.com/Pyomo/mpi-sppy) package provides generic
solvers for stochastic programming. `mpi-sppy` leverages the fact that
Pyomo's modeling objects are embedded within a full-featured high-level
programming language, which allows for transparent parallelization of
subproblems using Python parallel communication libraries.

* [Pyomo Home](http://www.pyomo.org)
* [About Pyomo](http://www.pyomo.org/about)
* [Download](http://www.pyomo.org/installation/)
* [Documentation](http://www.pyomo.org/documentation/)
* [Performance Plots](https://pyomo.github.io/performance/)
