---
tag: HSD6FKCYRC
kind: statement
role: theorem
name: Freedman's classification of simply connected 4-manifolds
msc: [57K40, 57N65]
uses: [8H58Q6YJCH, QQQ9B1DK4P, S1XK3HXHFX, WK8GKRKAVD, 0AXZNE5XNH, E4NJER1RFQ, 0QT00PB5G2]
about: [8H58Q6YJCH, WK8GKRKAVD]
sources:
  - url: https://en.wikipedia.org/wiki/4-manifold
---

## Statement

A *unimodular form* is a [[symmetric bilinear form|0AXZNE5XNH]] $Q \colon \Z^n \times \Z^n \to \Z$ whose matrix has determinant $\pm 1$.
It is *even* if $Q(x, x)$ is even for all $x \in \Z^n$, and *odd* otherwise.

1. For every unimodular form $Q$ there is a closed, simply connected, topological [[4-manifold|8H58Q6YJCH]] whose [[intersection form|WK8GKRKAVD]] is isomorphic to $Q$.
2. Two closed, simply connected, topological $4$-manifolds are [[homeomorphic|0QT00PB5G2]] if and only if their intersection forms are isomorphic and their [[Kirby–Siebenmann invariants|E4NJER1RFQ]] in $\Z/2$ are equal.
3. If $Q$ is even, there is exactly one such manifold with form $Q$ up to homeomorphism. If $Q$ is odd, there are exactly two, one with each value of the Kirby–Siebenmann invariant.

## Remarks

Michael Freedman proved the theorem in 1982.
The main step is his proof that Casson handles are homeomorphic to standard open handles, which makes the topological h-cobordism theorem hold for simply connected $4$-manifolds.
For an even form, the Kirby–Siebenmann invariant equals the signature divided by $8$, modulo $2$, so it is determined by $Q$.
The manifold with odd form and Kirby–Siebenmann invariant $1$ admits no smooth structure.
For example, the form $(1)$ is realized by the complex projective plane $\C P^2$ and by a fake $\C P^2$ that is not homeomorphic to it.
The [[$E_8$ manifold|BNDRN0G9BR]] realizes the $E_8$ form.
The case $Q = 0$ of rank $0$ is the four-dimensional topological Poincaré conjecture: a homotopy $4$-sphere is homeomorphic to $S^4$.

## Explanations

### L1 human

In dimension four, the way surfaces cross inside a manifold is recorded by a square table of integers, the intersection form.
Freedman's theorem says that, for manifolds without loops that cannot be contracted, this table and one extra bit decide the manifold up to continuous deformation.
Every possible table occurs.

### L2 human

The theorem reduces the topological classification of closed simply connected $4$-manifolds to the algebra of unimodular forms over $\Z$.
Indefinite forms are classified by rank, signature and type, so these manifolds are well understood.
The smooth picture is very different: [[Donaldson's theorem|34B7K77P31]] and [[Rokhlin's theorem|12BXVH5W5H]] show that many of Freedman's manifolds have no smooth structure.
Together the two results give [[exotic $\R^4$|X44PNC38E2]].
