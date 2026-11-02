---
tag: EGBAZMS66W
kind: statement
role: theorem
name: Maximum principle for potentials
msc: [31B15, 31A15]
uses: [HZNEQQBCW4, DCMFQ01QGS, FQTXV6BQZG, GPJC1NY5RE]
about: [DCMFQ01QGS]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_principle
---

## Statement

Let $n \ge 3$ and let $\mu$ be a positive [[Radon measure|HZNEQQBCW4]] on $\R^n$ with compact [[support|FQTXV6BQZG]] $S$.
Let
$$U^\mu(x) = \int_{\R^n} \abs{x - y}^{2-n} \, d\mu(y)$$
be its [[Newtonian potential|DCMFQ01QGS]], with values in $[0, \infty]$.
Let $M$ be a real number with $U^\mu(x) \le M$ for every $x \in S$.
Then $U^\mu(x) \le M$ for every $x \in \R^n$.

## Remarks

Proof idea: first assume that $U^\mu$ restricted to $S$ is continuous.
The [[continuity principle|GPJC1NY5RE]] then makes $U^\mu$ continuous on $\R^n$.
On the open set $\R^n \setminus S$ the potential is harmonic, it is at most $M$ on the boundary, which lies in $S$, and it tends to $0$ at infinity.
The maximum principle for harmonic functions gives $U^\mu \le M$ there.
The general case follows by restricting $\mu$ to compact subsets of $S$ on which $U^\mu$ is continuous, which exist by Lusin's theorem, and letting these subsets increase.

Example: let $\mu$ be the uniform measure of total mass $m$ on the unit sphere in $\R^3$.
By the shell theorem, $U^\mu(x) = m$ for $\abs{x} \le 1$ and $U^\mu(x) = m / \abs{x}$ for $\abs{x} \ge 1$.
So $U^\mu \le m$ on the support, and indeed $U^\mu \le m$ everywhere.

The positivity of $\mu$ is needed.
Let $\sigma$ be the uniform probability measure on the unit sphere of $\R^3$ and let $\mu = -\sigma$.
Then $U^\mu = -1$ on the support, but $U^\mu(x) = -1/\abs{x} > -1$ for $\abs{x} > 1$.
For logarithmic potentials in the plane the same statement holds: if $\int \log(1/\abs{z - w}) \, d\mu(w) \le M$ on the support of $\mu$, then it is at most $M$ on all of $\C$.

## Explanations

### L1 human

The potential of a positive charge is largest on the charge itself.
If the potential stays below a level $M$ wherever there is charge, it stays below $M$ everywhere in space.
This is the potential-theory version of the fact that a harmonic function has no interior maximum.

### L2 human

The principle is due to Maria and to Frostman.
It is the key step that turns an inequality on the support of a measure into an inequality everywhere.
It is used in the proof of Frostman's theorem to show that the equilibrium potential never exceeds its value on the conductor.
For Riesz kernels $\abs{x - y}^{\alpha - n}$ with $0 < \alpha < n$ and $\alpha > 2$, only a weaker version holds, with $M$ replaced by a constant multiple of $M$.
