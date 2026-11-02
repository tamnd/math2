---
tag: YD8SA6WS01
kind: concept
name: Adjoint state method
msc: [49M41, 65K10, 49K20]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_state_method
same_as:
  wikidata: Q4683172
  wikipedia: Adjoint state method
---

## Summary

The adjoint state method computes the [[gradient|0ABK9V9Y64]] of an objective that depends on parameters through the solution of an equation.
A typical example of such an equation is a discretised differential equation.
Instead of differentiating the state with respect to each parameter, it solves one extra linear equation, the adjoint equation, whose solution is the adjoint state.
The cost of the gradient is then about that of one or two state solves, whatever the number of parameters.
It is the basis of PDE-constrained optimization, of seismic and medical inversion, and of reverse-mode differentiation.

## Explanations

### L1 human

Suppose a simulation turns a million parameters into a state, and you measure how far the state is from data.
Changing each parameter one at a time and re-running the simulation would take a million runs.
The adjoint method runs the simulation once, then runs one extra backward problem that tells how sensitive the misfit is to the state.
From that single answer it reads off the sensitivity to all parameters at once.
In the simplest case, the state is $u = A^{-1} \theta$ and the misfit is $\frac{1}{2} \abs{u - d}^2$; then the gradient is the solution $\lambda$ of $A^T \lambda = u - d$.
