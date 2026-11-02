---
tag: GPJC1NY5RE
kind: statement
role: theorem
name: Continuity principle
msc: [31B15, 31A15]
uses: [HZNEQQBCW4, DCMFQ01QGS, FQTXV6BQZG]
about: [DCMFQ01QGS]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_theory
---

## Statement

Let $n \ge 3$ and let $\mu$ be a positive [[Radon measure|HZNEQQBCW4]] on $\R^n$ with compact [[support|FQTXV6BQZG]] $S$.
Let $U^\mu(x) = \int \abs{x - y}^{2-n} \, d\mu(y)$ be its [[Newtonian potential|DCMFQ01QGS]].
Let $x_0 \in S$, and assume that the restriction of $U^\mu$ to $S$ is continuous at $x_0$, with $U^\mu(x_0) < \infty$.
Then $U^\mu$, as a function on all of $\R^n$, is continuous at $x_0$.

## Remarks

This result is also called the Evans–Vasilesco theorem.
Proof idea: split $\mu$ into the part $\mu_1$ on a small ball $B(x_0, \delta)$ and the rest $\mu_2$.
The potential of $\mu_2$ is continuous near $x_0$, since its kernel is continuous there.
For $x$ near $x_0$, let $y$ be a point of $S$ nearest to $x$; every $z \in S$ satisfies $\abs{y - z} \le 2 \abs{x - z}$, so $U^{\mu_1}(x) \le 2^{n-2} U^{\mu_1}(y)$.
The continuity on $S$ and $U^\mu(x_0) < \infty$ make $U^{\mu_1}$ small on $S$ near $x_0$ when $\delta$ is small, hence also off $S$, and lower semicontinuity of $U^\mu$ gives the other inequality.

Example: for the uniform measure $\sigma$ of mass $1$ on the unit sphere in $\R^3$, the potential equals $1$ on the sphere, so its restriction to the support is continuous.
The theorem then says that $U^\sigma$ is continuous on $\R^3$, and indeed $U^\sigma(x) = \min(1, 1/\abs{x})$.

Without the hypothesis on the restriction, the potential can be discontinuous at a point of finite potential.
In $\R^3$, fix a ray from $x_0$ and let $c_k$ be its point at distance $2^{-k}$ from $x_0$.
Let $\sigma_k$ be the uniform probability measure on the sphere of radius $4^{-k}$ centred at $c_k$, and let $\mu = \sum_{k \ge 2} k \, 4^{-k} \sigma_k$.
Then $U^\mu(x_0) \le \sum_k k \, 4^{-k} / (2^{-k} - 4^{-k}) < \infty$.
But $U^\mu(c_k) \ge k$, and $c_k \to x_0$.
The same statement holds for logarithmic potentials in the plane.

## Explanations

### L1 human

A potential is always lower semicontinuous, but it may jump up near points where the charge is concentrated.
The continuity principle says that such jumps can only be seen from the charge itself.
If the potential behaves continuously when one stays on the charge, it behaves continuously when one comes from any direction.

### L2 human

The principle reduces questions of continuity of potentials to the support of the measure.
It is used in the proof of the maximum principle for potentials, to pass from inequalities on the support to inequalities everywhere.
