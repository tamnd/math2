---
tag: 4NCB2ZY08G
kind: counterexample
name: Lewy's example
msc: [35A01, 35F05, 32V05]
uses: [GC5BDZ6QBC, X7GP9BECD8]
sources:
  - url: https://en.wikipedia.org/wiki/Lewy%27s_example
same_as:
  wikidata: Q814880
  wikipedia: Lewy's example
---

## Counterexample

On $\R^3$ with coordinates $(x, y, t)$, consider the first-order linear operator
$$L = \frac{\partial}{\partial x} + i \frac{\partial}{\partial y} - 2i(x + iy) \frac{\partial}{\partial t}.$$
Its coefficients are polynomials, so they are smooth and even real-analytic.
Hans Lewy proved that there is a function $f \in C^\infty(\R^3)$ with the following property.
The [[partial differential equation|GC5BDZ6QBC]] $Lu = f$ has no solution $u$ of class $C^1$ on any nonempty open subset of $\R^3$.
So a linear partial differential equation with smooth coefficients and a smooth right-hand side need not be locally solvable.

## Remarks

The key step concerns right-hand sides that depend only on $t$.
If $\psi$ is a real-valued $C^1$ function of $t$ and $Lu = \psi'(t)$ has a $C^1$ solution near the origin, then $\psi$ is real-analytic near $t = 0$.
Choosing $\psi$ smooth but not real-analytic gives an equation with no solution near the origin; a Baire category argument then produces one $f$ that works at every point.
The operator $L$ is, up to a constant factor, the [[tangential Cauchy–Riemann operator|X7GP9BECD8]] of the hypersurface $\set{(z, w) \in \C^2 : \operatorname{Im} w = \abs{z}^2}$, written in the coordinates $z = x + iy$ and $t = \operatorname{Re} w$.
This contrasts with the Cauchy–Kovalevskaya theorem, which gives local solutions when the coefficients and the data are all real-analytic.
Hörmander later explained the phenomenon by a necessary condition for local solvability involving the commutator of $L$ and its complex conjugate $\bar L$.

## Explanations

### L1 human

Before this example, it was widely expected that a linear differential equation with nice coefficients always has solutions at least on small regions.
Lewy wrote down a simple equation in three real variables, with polynomial coefficients, that has no solution at all near any point for a suitable smooth right-hand side.
The obstruction comes from complex analysis: solutions would force certain smooth functions to be real-analytic, which they need not be.
