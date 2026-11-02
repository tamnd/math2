---
tag: RH8BD7PW5F
kind: concept
name: Butcher tableau
msc: [65L06]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_Runge%E2%80%93Kutta_methods
---

## Summary

A Butcher tableau is the table of coefficients that specifies a [[Runge–Kutta method|7DBPJKYC6C]].
It lists the nodes $c_i$ in a column, the matrix $(a_{ij})$ beside them, and the weights $b_i$ in a bottom row.
Its shape shows at a glance whether the method is explicit, with $(a_{ij})$ strictly lower triangular, or implicit.
Order conditions, stability functions and the algebraic theory of the [[Butcher group|6MH1DHMCPF]] are all expressed in terms of these coefficients.

## Explanations

### L1 human

A Runge–Kutta method mixes several slope evaluations within each step.
The Butcher tableau is a compact recipe that says where in the step each slope is measured and how the slopes are combined.
For example, the tableau with nodes $0, 1$, the single entry $a_{21} = 1$, and weights $\frac12, \frac12$ is [[Heun's method|RJEK60G28F]].
Different tables give different methods, and catalogues of methods are usually written as lists of tableaux.
