---
tag: 6DG4CTGXJD
kind: statement
role: theorem
name: Runge's theorem
msc: ["30E10", 41A20]
uses: [00R0X1WGPX, 0DG0Z72CQD, 0WCZH4AFMT, 08HJRTG5N7, 0D939CMME7]
about: [0DG0Z72CQD, 0WCZH4AFMT]
sources:
  - url: https://en.wikipedia.org/wiki/Runge%27s_theorem
same_as:
  wikidata: Q1505529
  wikipedia: Runge's theorem
---

## Statement

Let $K \subseteq \C$ be a [[compact set|00R0X1WGPX]].
Let $f$ be a [[holomorphic function|0DG0Z72CQD]] on an open set containing $K$.
Let $A \subseteq \C \setminus K$ be a set that contains at least one point of each bounded connected component of $\C \setminus K$.
Then for every $\varepsilon > 0$ there is a [[rational function|0WCZH4AFMT]] $r$ whose poles all lie in $A$ such that
$$\abs{f(z) - r(z)} < \varepsilon \quad \text{for all } z \in K.$$
In particular, if $\C \setminus K$ is [[connected|0D939CMME7]], then $f$ is a [[uniform limit|08HJRTG5N7]] on $K$ of polynomials.

## Remarks

Proof idea: by the Cauchy integral formula over a cycle around $K$, $f$ is a uniform limit on $K$ of finite sums of terms $c/(z - a)$ with $a$ off $K$.
Each pole $a$ can then be moved to a point of $A$ in the same component of $\C \setminus K$, by expanding in power series.
For the unbounded component, the pole is moved to $\infty$ instead.
A pole at $\infty$ means a polynomial.

The hypothesis on $A$ is necessary.
Let $K$ be the unit circle and $f(z) = 1/z$; the bounded component of $\C \setminus K$ is the open disc.
For every polynomial $p$ one has $\oint_K p(z) \, dz = 0$, while $\oint_K z^{-1} \, dz = 2\pi i$.
If $\abs{p - 1/z} < \varepsilon$ on $K$, then $2\pi = \abs{\oint_K (z^{-1} - p(z)) \, dz} \le 2\pi \varepsilon$, which fails for $\varepsilon < 1$.
With $A = \set{0}$ the rational function $r(z) = 1/z$ itself has its only pole in $A$ and approximates $f$ exactly.

## Explanations

### L1 human

A holomorphic function near a compact set can be approximated, uniformly on the set, by rational functions.
The poles of the rational functions are only needed inside the holes of the set, one chosen point per hole being enough.
If the set has no holes, polynomials are enough.
The circle example shows that holes really matter.

### L2 human

Runge's theorem is the starting point of approximation theory in the complex plane.
It is used to build holomorphic functions with prescribed properties, for example sequences of polynomials that converge pointwise on $\C$ to a discontinuous limit.
It gives the existence of solutions of the $\bar\partial$-equation and the Mittag-Leffler theorem on general open sets.
[[Mergelyan's theorem|5KKCSZJC29]] strengthens the polynomial case to functions that are only continuous on $K$ and holomorphic in its interior.
