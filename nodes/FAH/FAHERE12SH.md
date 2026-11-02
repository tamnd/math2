---
tag: FAHERE12SH
kind: definition
name: f-ring
msc: ["06F25"]
defines: VHHMZPNVEA
uses: [A0NP6HQNPX, WH4SFAACAS, 0P27W9RW0G]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_ordered_ring
---

## Definition

A *lattice-ordered ring* is a [[partially ordered ring|A0NP6HQNPX]] $(R, \le)$ whose order is a [[lattice|WH4SFAACAS]], with meet $\wedge$ and join $\vee$.
A lattice-ordered ring $R$ is an *f-ring* if for all $a, b, c \in R$,
$$a \wedge b = 0 \text{ and } c \ge 0 \implies ca \wedge b = 0 \text{ and } ac \wedge b = 0.$$

## Remarks

Example: the ring $C(X)$ of [[continuous real functions|0P27W9RW0G]] on a topological space $X$, with the pointwise order, is an f-ring.
If $\min(a, b) = 0$ pointwise and $c \ge 0$, then at each point where $b > 0$ one has $a = 0$, so $ca = 0$ there, and $\min(ca, b) = 0$.
Non-example: the ring of real $2 \times 2$ matrices with the entrywise order is lattice-ordered but is not an f-ring.
Let $E_{ij}$ be the matrix unit; then $E_{11} \wedge E_{21} = 0$ and $E_{21} \ge 0$, but $E_{21} E_{11} = E_{21}$ and $E_{21} \wedge E_{21} = E_{21} \ne 0$.
Every totally ordered ring is an f-ring, and in an f-ring every square is nonnegative.
