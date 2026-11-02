---
tag: 77VNNV4VET
kind: statement
role: theorem
name: Capacity and Hausdorff dimension
msc: [31B15, 28A78]
uses: [0R6EWFKRCF, 059TJN0NZ1, Q1TGZK8RN6, SSNFTHZ6YJ, 835MPDJXMA, FYNFT90NT2]
about: [SSNFTHZ6YJ, 835MPDJXMA]
sources:
  - url: https://en.wikipedia.org/wiki/Frostman_lemma
---

## Statement

Let $K \subseteq \R^n$ be a [[compact set|0R6EWFKRCF]] and let $0 < s < n$.
For a Borel [[probability measure|059TJN0NZ1]] $\mu$ on $K$, let
$$I_s(\mu) = \int_K \int_K \abs{x - y}^{-s} \, d\mu(x) \, d\mu(y)$$
be its [[Riesz energy|835MPDJXMA]] of order $s$.
The Riesz $s$-capacity of $K$ is $C_s(K) = \sup_\mu 1 / I_s(\mu)$, with $1/\infty = 0$.
Let $\mathcal{H}^s$ be the $s$-dimensional [[Hausdorff measure|Q1TGZK8RN6]] and $\dim_H$ the [[Hausdorff dimension|SSNFTHZ6YJ]].

1. If $\mathcal{H}^s(K) < \infty$, then $C_s(K) = 0$.
2. If $\dim_H K > s$, then $C_s(K) > 0$.

Hence $\dim_H K = \sup \set{ s \in (0, n) : C_s(K) > 0 } = \inf \set{ s \in (0, n) : C_s(K) = 0 }$ whenever $0 < \dim_H K < n$.

## Remarks

Proof idea for part 2: choose $t$ with $s < t < \dim_H K$.
Then $\mathcal{H}^t(K) > 0$, and the [[Frostman lemma|FYNFT90NT2]] gives a nonzero measure $\mu$ on $K$ with $\mu(B(x, r)) \le r^t$ for all balls.
Write $\int \abs{x - y}^{-s} \, d\mu(y) = \int_0^\infty \mu(B(x, \rho^{-1/s})) \, d\rho$.
The bound on balls shows that this integral is bounded in $x$, so $I_s(\mu) < \infty$ after normalizing $\mu$.
For part 1, a measure with finite $s$-energy satisfies $\mu(B(x, r)) / r^s \to 0$ as $r \to 0$ for $\mu$-almost every $x$.
A density theorem for Hausdorff measure shows that this is impossible when $\mathcal{H}^s(K) < \infty$ and $\mu \ne 0$.

Example: for $n \ge 3$ and $s = n - 2$, the capacity $C_{n-2}$ has the same null sets as the Newtonian capacity.
So a compact set with $\mathcal{H}^{n-2}(K) < \infty$, such as a segment in $\R^3$, has Newtonian capacity zero.
A compact set of Hausdorff dimension greater than $n - 2$, such as a flat disc in $\R^3$, has positive Newtonian capacity.

Neither part can be reversed in general: a set with $\dim_H K = s$ may have $C_s(K) = 0$ or $C_s(K) > 0$, depending on finer properties of the set.

## Explanations

### L1 human

Capacity and Hausdorff dimension both measure how thin a set is.
The theorem says they draw the line in the same place.
A set of dimension bigger than $s$ can carry a charge with finite $s$-energy, and a set with finite $s$-dimensional measure cannot.
In space, Newtonian capacity corresponds to $s = 1$: smooth curves are too thin, smooth surfaces are thick enough.

### L2 human

The result turns questions about capacity into questions about dimension and back.
It is the basis of the energy method for lower bounds of Hausdorff dimension, used in the study of projections and of Brownian paths.
In potential theory it shows that removable and exceptional sets, which are defined through capacity, are always small in the sense of dimension.
In the plane the logarithmic capacity sits at the level $s = 0$: every compact set of positive Hausdorff dimension has positive logarithmic capacity.
