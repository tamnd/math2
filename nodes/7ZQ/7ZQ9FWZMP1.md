---
tag: 7ZQ9FWZMP1
kind: statement
role: theorem
name: Bishop's theorem on analytic sets
msc: [32D15, 32B15, 32C25]
uses: [VMDTGTMN9P, C2R5Q2Q717, JSGWAN2RJV, Q1TGZK8RN6]
about: [GB7M582M5Y]
sources:
  - url: https://en.wikipedia.org/wiki/Remmert%E2%80%93Stein_theorem
---

## Statement

Let $X$ be an open subset of $\C^n$, let $E$ be an [[analytic subset|VMDTGTMN9P]] of $X$, and let $k \ge 1$ be an integer.
Let $A$ be an analytic subset of $X \setminus E$ of [[pure dimension|C2R5Q2Q717]] $k$.
Suppose that every point of $E$ has a neighbourhood $W$ in $X$ such that $\mathcal{H}^{2k}(A \cap W) < \infty$, where $\mathcal{H}^{2k}$ is the $2k$-dimensional [[Hausdorff measure|Q1TGZK8RN6]] on $\C^n = \R^{2n}$.
Then the closure $\overline{A}$ of $A$ in $X$ is an analytic subset of $X$, of pure dimension $k$.

## Remarks

No condition on the dimension of $E$ is needed; it is replaced by the condition that $A$ has locally finite $2k$-dimensional volume near $E$.
The idea of the proof is to use the volume bound to control generic linear projections to $\C^k$.
Near each point of $E$, the closure $\overline{A}$ then projects properly, with a bounded number of sheets.
The symmetric functions of the sheets are bounded holomorphic functions outside a thin set, and they extend.
Example: let $E = \set{z_1 = 0}$ in $\C^2$ and $A = \set{z_2 = 0,\ z_1 \ne 0}$; the area of $A$ in each ball is finite, and indeed $\overline{A}$ is the $z_1$-axis.
The volume hypothesis is needed: for $A = \set{(z_1, e^{1/z_1}) : z_1 \ne 0}$ and the same $E$, the closure $A \cup E$ is not analytic, so by the theorem $A$ has infinite area near every point of $E$.
The theorem also holds with $X$ a complex manifold, since the statement is local.

## Explanations

### L1 human

An analytic set known outside an exceptional analytic set extends across it, as long as it has finite area, or finite volume in the right dimension, near the exceptional set.
A curve spiralling wildly towards a line, like the graph of $e^{1/z}$ near $z = 0$, has infinite area and does not extend.
Finite volume rules out this kind of wild behaviour.

### L2 human

Bishop's theorem strengthens the Remmert–Stein theorem, in which the exceptional set must have smaller dimension than $A$.
Volume bounds of this kind come naturally from Wirtinger's inequality and Stokes' theorem, which makes the theorem useful for limits of analytic cycles.
It is a main step in proving that limits of complex analytic cycles with bounded volume are analytic.
