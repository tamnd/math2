---
tag: QQ62R5ZAXJ
kind: concept
name: Boundary integral method for the Dirichlet problem
msc: [31B10, 31A10, 45B05]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_element_method
---

## Summary

The boundary integral method solves the [[Dirichlet problem|8D56GQ4AG8]] for the Laplace equation with a [[double layer potential|EG8Z3FWV9A]].
The unknown harmonic function is written as that potential, with an unknown density on the boundary.
The [[jump relations|J58YA8QNNX]] turn the boundary condition into a Fredholm integral equation of the second kind for the density.
The [[Fredholm alternative|4HH8C9V8JQ]] then reduces existence of a solution to uniqueness.
Its discretisation is the boundary element method of numerical analysis.

## Explanations

### L1 human

Instead of looking for a function everywhere inside a region, look only for a function on its boundary.
Spread unknown dipoles over the boundary; whatever their strengths, they produce a harmonic function inside.
Then choose the strengths so that this function has the prescribed values on the boundary, which is one equation on the boundary only.
For the unit ball in space and boundary value $1$, the constant density $-1$ does the job, and the potential it produces is $1$ throughout the ball.
