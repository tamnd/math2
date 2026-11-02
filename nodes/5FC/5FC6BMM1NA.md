---
tag: 5FC6BMM1NA
kind: concept
name: Classification of second-order PDEs
msc: [35A99, 35J15, 35L10]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_differential_equation
---

## Summary

Linear second-order partial differential equations are sorted into elliptic, parabolic and hyperbolic equations.
The type is given by the signs of the eigenvalues of the matrix of second-order coefficients.
The three types behave very differently: elliptic equations describe equilibria, parabolic equations describe diffusion, and hyperbolic equations describe waves.
The model cases are the [[Laplace equation|S8RG6N1PRT]], the [[heat equation|VP2HN86VAG]] and the [[wave equation|5EHD2XBQDG]].
See the [[definition|J53A2A04P7]].

## Explanations

### L1 human

In two variables the second-order part $A u_{xx} + 2B u_{xy} + C u_{yy}$ looks like the quadratic form $A x^2 + 2B xy + C y^2$.
Such a form describes an ellipse, a parabola or a hyperbola, depending on the sign of $AC - B^2$, and the names of the PDE types come from this.
For $u_{xx} + u_{yy}$ one has $AC - B^2 = 1 > 0$, an ellipse, and the equation is elliptic.
For $u_{xx} - u_{yy}$ one has $AC - B^2 = -1 < 0$, a hyperbola, and the equation is hyperbolic.
The type tells which extra data, such as boundary values or initial values, give a good problem.
