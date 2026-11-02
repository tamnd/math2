---
tag: W6SXM59TS4
kind: statement
role: theorem
name: Kellogg–Evans theorem
msc: [31B25, 31B15, 31B20]
uses: [B7948M365K, C95QJ7YH5T, 02BH3MCBQB, 05D5EGMFYV]
about: [B7948M365K, C95QJ7YH5T]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_set_(potential_theory)
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]].
Call a point of the [[boundary|05D5EGMFYV]] $\partial\Omega$ irregular if it is not a [[regular boundary point|B7948M365K]].
Then the set of irregular points of $\partial\Omega$ is a [[polar set|C95QJ7YH5T]].

## Remarks

Polar sets have capacity zero, so they are very small: they have Lebesgue measure zero, and in $\R^n$ with $n \ge 3$ they have Hausdorff dimension at most $n - 2$.
Consequence: for each continuous $f$ on $\partial\Omega$, the Perron–Wiener–Brelot solution $H_f$ tends to $f(\xi)$ at every boundary point $\xi$ outside a polar set, that is, quasi-everywhere.
So the generalized solution solves the Dirichlet problem up to an exceptional set of capacity zero.
Example: for the punctured ball, the irregular set is $\set{0}$, a single point, which is polar.
Example: for the [[Lebesgue spine|EFFC7688KR]], the only irregular point is the tip of the spike.

## Explanations

### L1 human

Some boundary points can be bad for the Dirichlet problem, but there are always very few of them.
They form a set so thin that electric charge cannot sit on it.
So the generalized solution takes the right boundary values almost everywhere, in the sense of capacity.

### L2 human

The theorem turns the Perron–Wiener–Brelot solution into a genuine solution off a negligible set.
It is the basis for treating boundary values quasi-everywhere in modern potential theory and in the theory of Sobolev spaces.
Its proof uses the fine topology or the equilibrium potential of compact parts of the boundary, together with the barrier characterization of regular points.
