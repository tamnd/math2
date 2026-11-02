---
tag: M1VKCW3RFW
kind: concept
name: Dbar operator
msc: [32W05]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_differential_form
---

## Summary

The $\bar\partial$ operator, read "d-bar", sends a [[$(p, q)$-form|DC81TCR98Y]] to a $(p, q+1)$-form by differentiating its coefficients in the conjugate variables $\bar z_1, \dots, \bar z_n$.
On functions it is $\bar\partial f = \sum_j \frac{\partial f}{\partial \bar z_j} \, d\bar z_j$, and $\bar\partial f = 0$ is exactly the system of [[Cauchy–Riemann equations in several variables|9PT772R94A]].
It satisfies $\bar\partial \circ \bar\partial = 0$ and splits the [[exterior derivative|0ZHSTAG8ZY]] as $d = \partial + \bar\partial$.
It generalises the one-variable [[Cauchy–Riemann operator|PPSSTHTEDE]], and it is the basic operator of Dolbeault cohomology and of the $L^2$ methods of several complex variables.

## Explanations

### L1 human

The exterior derivative $d$ measures how a function or form changes in all real directions.
Using complex coordinates, this change splits into a part along $z_1, \dots, z_n$ and a part along $\bar z_1, \dots, \bar z_n$.
The $\bar\partial$ operator keeps only the second part.
A function is holomorphic exactly when this part is zero.
For example, $\bar\partial(z_1 \bar z_2) = z_1 \, d\bar z_2$, which is not zero, so $z_1 \bar z_2$ is not holomorphic.
