---
tag: KS4FJ6H5JH
kind: example
name: Hénon map
msc: [37F80, 37D45, 32H50]
instance_of: [2J7JB3H3FD]
uses: [6WCRMYEYF9, 0ZCSMYHTBP, 9WKCZGG906]
sources:
  - url: https://en.wikipedia.org/wiki/H%C3%A9non_map
same_as:
  wikidata: Q1642961
  wikipedia: Hénon map
---

## Example

For parameters $a, b$, the *Hénon map* is
$$H_{a,b}(x, y) = (1 - a x^2 + y, \; b x).$$
Hénon studied it for real $a, b$ as a model of a dissipative system; for $a = 1.4$ and $b = 0.3$ its orbits accumulate numerically on a [[strange attractor|9WKCZGG906]].

For complex $a, b$ with $b \ne 0$, $H_{a,b}$ is a holomorphic automorphism of $\C^2$.
Check: if $(u, v) = H_{a,b}(x, y)$, then $x = v/b$ and $y = u - 1 + a v^2/b^2$, so $H_{a,b}$ is a bijection with polynomial inverse
$$H_{a,b}^{-1}(u, v) = \left(\frac{v}{b}, \; u - 1 + \frac{a v^2}{b^2}\right).$$
Its Jacobian matrix is $\begin{pmatrix} -2ax & 1 \\ b & 0 \end{pmatrix}$, with [[Jacobian determinant|0ZCSMYHTBP]] $-b$, a nonzero constant.
For real $a, b$ it multiplies area in $\R^2$ by $\abs{b}$, so for $\abs{b} < 1$ it contracts area.
As a map of $\C^2$ it multiplies volume by $\abs{b}^2$.

## Remarks

In complex dynamics one often writes generalized Hénon maps as $(x, y) \mapsto (p(x) - a y, x)$ with $p$ a polynomial of degree $d \ge 2$ and $a \ne 0$.
Friedland and Milnor showed that every polynomial automorphism of $\C^2$ is conjugate either to a map of a simple triangular form or to a composition of generalized Hénon maps.
So Hénon maps are the main objects of [[holomorphic dynamics in several variables|6WCRMYEYF9]] on $\C^2$.
For them one studies the sets $K^\pm$ of points whose forward or backward orbits stay bounded, and the Julia sets $J^\pm = \partial K^\pm$.

## Explanations

### L1 human

The Hénon map folds the plane and squeezes it, then applies the same rule again.
Unlike the logistic map, it can be undone: from the image point one recovers the starting point by a formula.
Even so, repeated application mixes points in a chaotic way, and for some parameters the orbits pile up on a fractal set.
Taken over the complex numbers, it is the simplest interesting invertible holomorphic map of two-dimensional complex space.
