---
tag: ARGZ549BQT
kind: definition
name: Möbius function of a poset
msc: [06A07, 05A19]
defines: 2Y75S8NG5B
uses: [TV1V4JDRDD, 1H9SFWHYEB]
sources:
  - url: https://en.wikipedia.org/wiki/Incidence_algebra
---

## Definition

Let $(P, \le)$ be a [[locally finite poset|TV1V4JDRDD]], and write $x < y$ when $x \le y$ and $x \ne y$.
The *Möbius function* of $P$ is the function $\mu \colon P \times P \to \Z$ given by:

1. $\mu(x, x) = 1$ for all $x \in P$.
2. $\mu(x, y) = -\sum_{x \le z < y} \mu(x, z)$ for $x < y$.
3. $\mu(x, y) = 0$ when $x \not\le y$.

## Remarks

Clause 2 is a recursion over the finite interval $[x, y]$, so $\mu$ is well defined.
Equivalently, $\mu$ is the inverse of the zeta function $\zeta$ in the [[incidence algebra|1H9SFWHYEB]] of $P$, where $\zeta(x, y) = 1$ for $x \le y$ and $0$ otherwise.
From this one also gets $\mu(x, y) = -\sum_{x < z \le y} \mu(z, y)$ for $x < y$.

Example: in the lattice of subsets of a finite set, $\mu(S, T) = (-1)^{\abs{T \setminus S}}$ for $S \subseteq T$.
Check: for $\abs{T \setminus S} = k \ge 1$, the sum $\sum_{S \subseteq U \subseteq T} (-1)^{\abs{U \setminus S}} = \sum_{j=0}^{k} \binom{k}{j} (-1)^j = (1 - 1)^k = 0$, as clauses 1 and 2 require.

Non-example: the function $\nu(x, y) = (-1)^{y - x}$ for $x \le y$ on the chain $\N$ is not the Möbius function.
It satisfies clause 1, but clause 2 fails at $(0, 2)$: there $\mu(0, 2) = -(1 - 1) = 0$, while $\nu(0, 2) = 1$.

For the positive integers ordered by divisibility, $\mu(d, n)$ is the number-theoretic Möbius function of $n / d$.
