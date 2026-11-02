---
tag: 3G1CJ6HJMK
kind: statement
role: theorem
name: Cheng–Yau gradient estimate
msc: [31C12, 58J05, 53C21]
uses: [7CBT4SM83Y, 4GTNM0WHDH, PK2KNMWNW3, 0ABK9V9Y64, N76R7JWMNJ, YNH832D50W]
about: [PK2KNMWNW3]
sources:
  - url: https://en.wikipedia.org/wiki/Harnack%27s_inequality
---

## Statement

Let $(M, g)$ be a complete [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$, and let $K \ge 0$ be a constant such that the [[Ricci curvature|4GTNM0WHDH]] satisfies $\operatorname{Ric} \ge -(n - 1) K g$.
Let $x_0 \in M$, let $R > 0$, and let $B(x_0, r)$ denote the geodesic ball of radius $r$ about $x_0$.
There is a constant $C_n$, depending only on $n$, with the following property.
If $u$ is a positive [[harmonic function|PK2KNMWNW3]] on $B(x_0, 2R)$, then
$$\frac{\abs{\nabla u}}{u} \le C_n \left( \frac{1}{R} + \sqrt{K} \right) \quad \text{on } B(x_0, R),$$
where $\nabla u$ is the [[gradient|0ABK9V9Y64]] of $u$.

## Remarks

The proof applies the Bochner formula to $w = \abs{\nabla \log u}^2$.
With the lower bound on Ricci curvature, it gives a lower bound for $\Delta w$ in which $w^2$ appears with a positive coefficient, up to terms in $\nabla w$ and $K w$.
One multiplies $w$ by a cutoff function of the distance to $x_0$ and applies the maximum principle at an interior maximum.
The Laplacian comparison theorem controls the Laplacian of the distance function in this step.
Example: if $\operatorname{Ric} \ge 0$, take $K = 0$ and let $R \to \infty$.
Then $\abs{\nabla u} = 0$ for every positive harmonic function $u$ on $M$, which is Yau's Liouville theorem: positive harmonic functions on a complete manifold with nonnegative Ricci curvature are constant.
Integrating the estimate along geodesics gives a Harnack inequality: $\sup_{B(x_0, R)} u \le e^{C_n (2 + 2\sqrt{K} R)} \inf_{B(x_0, R)} u$.
The term $\sqrt{K}$ cannot be dropped: on the hyperbolic upper half-plane, where $\operatorname{Ric} = -g$, the positive harmonic function $u = y$ has $\abs{\nabla u}/u = 1$ everywhere.

## Explanations

### L1 human

A positive harmonic function cannot change too fast compared with its own size.
The theorem gives a precise limit on the relative rate of change.
It is at most a constant over the radius of the ball, plus a term that depends on how negative the curvature can be.
On a space with no negative curvature and infinite size, the limit tends to $0$, so positive harmonic functions must be constant.
This explains why such spaces resemble Euclidean space from the point of view of harmonic functions.

### L2 human

The estimate is a geometric form of the [[gradient estimates for harmonic functions|N76R7JWMNJ]] in $\R^n$ and of [[Harnack's inequality|YNH832D50W]].
Its proof, through the Bochner formula and a maximum principle, became a model for many later estimates, such as the Li–Yau estimate for positive solutions of the heat equation.
It gives Liouville theorems, Harnack inequalities and control of the growth of harmonic functions in terms of curvature.
