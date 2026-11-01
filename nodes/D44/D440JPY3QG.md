---
tag: D440JPY3QG
kind: counterexample
name: Tychonoff plank
msc: [54G20, 54D15, 54F05]
uses: [0YSCSX5YZC, 0GBG8B49AA, 0TVJZYB6SH, 0S1FJ8VEX9, 0NSR9V8TED, 0WS9P12FQR, C5N2J2K6Z3]
sources:
  - url: https://en.wikipedia.org/wiki/Tychonoff_plank
---

## Counterexample

Let $\omega$ be the first infinite [[ordinal|0YSCSX5YZC]] and $\omega_1$ the first uncountable ordinal.
Give $[0, \omega_1]$ and $[0, \omega]$ the order topology, and let $T = [0, \omega_1] \times [0, \omega]$ with the [[product topology|0GBG8B49AA]].
This is the Tychonoff plank.
The deleted Tychonoff plank is the [[subspace|0WS9P12FQR]] $T_\infty = T \setminus \set{(\omega_1, \omega)}$.
The plank $T$ is [[compact|0TVJZYB6SH]] and [[Hausdorff|0S1FJ8VEX9]], hence [[normal|0NSR9V8TED]], but the open subspace $T_\infty$ is not normal.

## Remarks

The sets $A = \set{\omega_1} \times [0, \omega)$ and $B = [0, \omega_1) \times \set{\omega}$ are disjoint and closed in $T_\infty$.
Let $U$ be an open set of $T_\infty$ containing $A$.
For each $n < \omega$ there is $\alpha_n < \omega_1$ with $(\alpha_n, \omega_1] \times \set{n} \subseteq U$.
The supremum $\alpha$ of the countably many $\alpha_n$ is still countable, so $\alpha + 1 < \omega_1$ and $(\alpha + 1, n) \in U$ for every $n$.
Any open set $V$ containing $(\alpha + 1, \omega) \in B$ contains $(\alpha + 1, n)$ for all large $n$, so $V$ meets $U$.
Hence $A$ and $B$ cannot be separated, and $T_\infty$ is not normal.
Since $T_\infty$ is a subspace of the compact Hausdorff space $T$, it is a [[Tychonoff space|C5N2J2K6Z3]]; so an open subspace of a normal space need not be normal.

## Explanations

### L1 human

The plank is a product of two well-ordered "lines", one countably long and one uncountably long, each with a top point.
It is compact, so it behaves well.
Removing the single top corner point leaves two edges that run towards the missing corner.
Any open set around one edge must swallow a whole column near the corner, and so it always touches the other edge.
