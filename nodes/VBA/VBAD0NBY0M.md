---
tag: VBAD0NBY0M
kind: definition
name: Regge calculus
msc: [83C27, 52B70]
defines: D1SK2X66FE
uses: [V8GZ0W1ZZ5, 05HN08ZSRJ, JPE3A1SN7V]
sources:
  - url: https://en.wikipedia.org/wiki/Regge_calculus
---

## Definition

Let $T$ be a [[simplicial complex|V8GZ0W1ZZ5]] that triangulates an $n$-manifold, $n \ge 2$.
Assign a positive length $l_e$ to each edge $e$.
Assume every simplex of $T$ can be realized as a simplex in Euclidean space $\R^n$ (or Minkowski space) with these edge lengths.
This makes $T$ a piecewise flat manifold.
For each $(n-2)$-simplex $h$ of $T$ (a hinge), the *deficit angle* is
$$\varepsilon_h = 2\pi - \sum_{\sigma \supset h} \theta_{\sigma, h}.$$
The sum runs over the $n$-simplices $\sigma$ containing $h$, and $\theta_{\sigma, h}$ is the [[dihedral angle|05HN08ZSRJ]] of $\sigma$ at $h$.
*Regge calculus* is the theory of the edge lengths with the Regge action
$$S_R = \frac{1}{8 \pi G} \sum_h \operatorname{vol}_{n-2}(h) \, \varepsilon_h,$$
whose field equations are $\partial S_R / \partial l_e = 0$ for every edge $e$.

## Remarks

The action approximates the [[Einstein–Hilbert action|JPE3A1SN7V]] $\frac{1}{16\pi G} \int R \sqrt{g}$, because the curvature of a piecewise flat manifold is a sum of delta functions on the hinges with $\int R \sqrt{g} = 2 \sum_h \operatorname{vol}(h) \varepsilon_h$.
By the Schläfli identity $\sum_h \operatorname{vol}(h) \, d\varepsilon_h = 0$, the field equations reduce to $\sum_h \varepsilon_h \, \partial \operatorname{vol}(h) / \partial l_e = 0$.
Example ($n = 2$): the surface of a regular tetrahedron has hinges at its four vertices.
At each vertex three equilateral triangles meet with angles $\pi/3$, so $\varepsilon = 2\pi - \pi = \pi$.
The total $4\pi$ equals $2\pi \chi(S^2)$, as the Gauss–Bonnet theorem requires.
Non-example: lengths $1, 1, 3$ on a triangle are not allowed, since they violate the triangle inequality and no flat triangle has these sides.
