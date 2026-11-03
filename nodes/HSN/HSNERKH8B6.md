---
tag: HSNERKH8B6
kind: definition
name: Ruppeiner geometry
msc: [80A10, 53B50, 82B30]
defines: YJQS3W1P71
uses: [SPY89W0RJ7, H9F9CNPBSN, 0SCSQWXRA4, 1R7ANBHDSN, YYQRRFQAQP]
sources:
  - url: https://en.wikipedia.org/wiki/Ruppeiner_geometry
---

## Definition

Let a thermodynamic system have [[entropy|SPY89W0RJ7]] $S(X^1, \dots, X^n)$ on an open domain $D \subseteq \R^n$.
Here $X^1, \dots, X^n$ are [[extensive variables|H9F9CNPBSN]], such as the internal energy, the volume and the amounts of the species.
Assume that $S$ is twice continuously differentiable.
Assume that the [[Hessian matrix|0SCSQWXRA4]] of $S$ is negative definite on $D$.
The *Ruppeiner metric* is the [[Riemannian metric|1R7ANBHDSN]] on $D$
$$g_R = -\sum_{i,j=1}^{n} \frac{\partial^2 S}{\partial X^i \partial X^j} \, dX^i \, dX^j.$$
*Ruppeiner geometry* is the Riemannian geometry of $(D, g_R)$.

## Remarks

The hypothesis of negative definiteness is the strict concavity of $S$, which is the local form of the [[thermodynamic stability conditions|YYQRRFQAQP]]; it makes $g_R$ positive definite.
If one variable is kept fixed, for example the amount of matter, one uses one variable fewer.
The reason is that $S$ is homogeneous of degree $1$, so its Hessian in all variables is singular.
The Ruppeiner metric is conformal to the Weinhold metric $g_W = \sum_{i,j} \frac{\partial^2 U}{\partial Y^i \partial Y^j} dY^i dY^j$, the Hessian of the internal energy $U$ in the variables $Y = (S, \dots)$: one has $g_R = g_W / T$, where $T$ is the temperature.

Example: for a monatomic ideal gas with fixed particle number $N$ and Boltzmann constant $k$, up to an additive constant $S = Nk \left( \tfrac{3}{2} \ln U + \ln V \right)$ in the variables $(U, V)$.
Then $g_R = \tfrac{3Nk}{2} \frac{dU^2}{U^2} + Nk \frac{dV^2}{V^2}$.
With $u = \ln U$ and $v = \ln V$ this is $\tfrac{3Nk}{2} du^2 + Nk \, dv^2$, a constant metric, so the scalar curvature is $0$.

Non-example: take a fluid in the region where $\kappa_T < 0$, such as the unstable part of a van der Waals isotherm.
There $S$ is not concave, the Hessian is not negative definite, and $g_R$ is not a Riemannian metric.
