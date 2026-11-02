---
tag: HTDYK465JA
kind: definition
name: Lusternik–Schnirelmann category
msc: [55M30, "58E05"]
defines: W5BHHXCYXA
uses: [0CNQXVBHCX, 049PXYHW1T, SMEV5BSQ5S]
sources:
  - url: https://en.wikipedia.org/wiki/Lusternik–Schnirelmann_category
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]].
An open subset $U \subseteq X$ is *contractible in $X$* if the inclusion $U \to X$ is [[null-homotopic|SMEV5BSQ5S]].
The *Lusternik–Schnirelmann category* $\operatorname{cat}(X)$ is the least integer $m \ge 0$ such that there is an [[open cover|049PXYHW1T]] $X = U_0 \cup U_1 \cup \cdots \cup U_m$ by $m + 1$ open sets, each contractible in $X$.
If no such finite cover exists, $\operatorname{cat}(X) = \infty$.

## Remarks

This is the normalized convention; some authors count the open sets instead, which adds $1$.
If $X$ is a path-connected space, $R$ is a commutative ring, and $H^*(X; R)$ has $m$ elements of positive degree with nonzero cup product, then $\operatorname{cat}(X) \ge m$.
The category is a homotopy invariant.

Example: for $n \ge 1$, $\operatorname{cat}(S^n) = 1$.
The sets $U_0 = S^n \setminus \set{N}$ and $U_1 = S^n \setminus \set{S}$, where $N$ and $S$ are the poles, cover $S^n$ and are homeomorphic to $\R^n$, hence contractible, hence contractible in $S^n$.
And $\operatorname{cat}(S^n) \ne 0$, since the identity of $S^n$ is not null-homotopic.

Non-example: the cover of $S^1$ by the single open set $U_0 = S^1$ does not show $\operatorname{cat}(S^1) = 0$, since the inclusion $S^1 \to S^1$ is the identity, which is not null-homotopic.

Other values: the torus $T^n = (S^1)^n$ and the real projective space $\R P^n$ both have category $n$.
