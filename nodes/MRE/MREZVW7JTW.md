---
tag: MREZVW7JTW
kind: statement
role: theorem
name: Grauert's semicontinuity theorem
msc: [32C35, 32G13]
uses: [HXSZA44J5J, DSJET02WPR, 15XEBGNGHC, PQ6Q143ARJ, RN4G8SGP6P, RNDDWDAFJ5, GB7M582M5Y, MPNGD4V271, ZNCF16AENG]
about: [DSJET02WPR, RN4G8SGP6P]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_sheaf_cohomology
---

## Statement

Let $f \colon X \to Y$ be a [[proper|15XEBGNGHC]] holomorphic map of [[complex analytic spaces|HXSZA44J5J]] and let $\mathcal{F}$ be a [[coherent analytic sheaf|DSJET02WPR]] on $X$.
Assume that $\mathcal{F}$ is flat over $Y$: for each $x \in X$ the stalk $\mathcal{F}_x$ is a flat module over $\mathcal{O}_{Y, f(x)}$.
For $y \in Y$ let $\mathfrak{m}_y \subseteq \mathcal{O}_{Y,y}$ be the maximal ideal.
Let $X_y = f^{-1}(y)$ be the fibre with the structure sheaf $\mathcal{O}_X / \mathfrak{m}_y \mathcal{O}_X$.
Let $\mathcal{F}(y) = \mathcal{F} / \mathfrak{m}_y \mathcal{F}$, a coherent sheaf on $X_y$.
For an integer $q \ge 0$ let $h^q(y) = \dim_\C H^q(X_y, \mathcal{F}(y))$.
Then:

1. for every $q \ge 0$ and every integer $k$, the set $\set{y \in Y : h^q(y) \ge k}$ is an [[analytic subset|GB7M582M5Y]] of $Y$; in particular $h^q$ is upper [[semicontinuous|RN4G8SGP6P]];
2. the [[Euler characteristic|RNDDWDAFJ5]] $y \mapsto \sum_{q \ge 0} (-1)^q h^q(y)$ is locally constant on $Y$.

## Remarks

Each $h^q(y)$ is finite by the [[Cartan–Serre finiteness theorem|MPNGD4V271]], since $X_y$ is compact.
The proof uses [[Grauert's direct image theorem|ZNCF16AENG]] in a refined form: locally on $Y$, the cohomology of all fibres is computed by one bounded complex of finite free $\mathcal{O}_Y$-modules.
Ranks of matrices of holomorphic functions can only drop on analytic subsets, which gives part 1, and the alternating sum of the ranks of the free modules gives part 2.

Example: let $E$ be a compact Riemann surface of genus $1$ and let $\mathcal{P}$ be the Poincaré line bundle on $E \times E$.
For $y \in E$, its restriction to $E \times \set{y}$ is a line bundle $L_y$ of degree $0$ on $E$, trivial exactly when $y = 0$.
For the projection $f \colon E \times E \to E$ onto the second factor, the fibre over $y$ is $E \times \set{y}$, and one gets $h^0(y) = h^1(y) = 1$ for $y = 0$ and $h^0(y) = h^1(y) = 0$ otherwise.
The dimensions jump up on the analytic set $\set{0}$, and the Euler characteristic is constantly $0$.

## Explanations

### L1 human

Consider a family of compact complex spaces with a coherent sheaf on each of them, varying holomorphically.
The dimensions of the cohomology groups may jump at special members of the family, but they can only jump up, and only on an analytic subset of the parameter space.
Their alternating sum does not change at all.

### L2 human

The theorem is a basic tool in deformation theory.
If $h^q$ is constant and $Y$ is reduced, then $R^q f_* \mathcal{F}$ is locally free and its fibre at $y$ is $H^q(X_y, \mathcal{F}(y))$.
This base change property is used to build vector bundles over moduli spaces.
It is the analytic counterpart of the semicontinuity theorem for flat proper morphisms of schemes.
