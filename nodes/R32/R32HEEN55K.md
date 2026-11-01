---
tag: R32HEEN55K
kind: statement
role: theorem
name: Liouville's theorems on elliptic functions
msc: ["33E05", 30D30]
uses: [FF9ZPCZ59K, 0JFGKKWWFK, 0WPQYW8MTE, 0EHKVRF4J6, 032HKYS329, 0PN2BXRS8G]
about: [FF9ZPCZ59K]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_function
    locator: Liouville's theorems
---

## Statement

Let $\Lambda = \Z\omega_1 + \Z\omega_2$ be a lattice in $\C$, with $\omega_1, \omega_2$ linearly independent over $\R$.
Let $f$ be an [[elliptic function|FF9ZPCZ59K]] with respect to $\Lambda$.
Let $P = \set{a + s\omega_1 + t\omega_2 : 0 \le s, t < 1}$ be a fundamental parallelogram, for some $a \in \C$.

1. If $f$ has no poles, then $f$ is constant.
2. The sum of the [[residues|0JFGKKWWFK]] of $f$ at its poles in $P$ is $0$.
3. If $f$ is not constant and $c \in \C$, then $f$ has as many solutions of $f(z) = c$ in $P$ as [[poles|0WPQYW8MTE]] in $P$, both counted with multiplicity.

## Remarks

1. An elliptic function without poles is continuous on the closure of $P$, hence bounded on $\C$ by periodicity, hence constant by [[Liouville's theorem|0EHKVRF4J6]].
2. By the [[residue theorem|032HKYS329]], the sum of the residues is $\frac{1}{2\pi i}\int_{\partial P} f(z)\,dz$, and the integrals over opposite sides cancel by periodicity.
3. Apply part 2 to the elliptic function $f'/(f - c)$ and use the [[argument principle|0PN2BXRS8G]].

The common number in part 3 is the *order* of $f$.
Part 2 shows that the order is never $1$: a single simple pole would have a nonzero residue.
So a nonconstant elliptic function has order at least $2$; the [[Weierstrass function|361NAK68QK]] $\wp$ has order $2$, with one double pole in $P$.
A further result of the same kind says that the sum of the zeros minus the sum of the poles in $P$, with multiplicity, lies in $\Lambda$.
Each point of $\C$ is congruent modulo $\Lambda$ to exactly one point of $P$, so the counts in parts 2 and 3 do not depend on $a$.
The contour arguments use a choice of $a$ for which $f$ has no zeros, poles or $c$-points on the boundary of $P$.

## Explanations

### L1 human

These three facts constrain what a doubly periodic function can look like.
It must have poles unless it is constant.
Its residues inside one period cell add up to zero.
And it takes every value the same number of times in a period cell.

### L2 human

All three proofs use one idea: integrate around the boundary of a period parallelogram, where opposite sides cancel by periodicity.
The results show that the smallest possible order of a nonconstant elliptic function is $2$.
This is why the Weierstrass function has a double pole and the Jacobi functions have two simple poles per cell.
On the torus $\C/\Lambda$, they are the first instances of general facts on compact Riemann surfaces.
There a holomorphic function is constant, and a meromorphic function has as many zeros as poles.
