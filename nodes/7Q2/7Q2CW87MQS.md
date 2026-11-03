---
tag: 7Q2CW87MQS
kind: definition
name: Plus construction
msc: [19D06, 55R35]
defines: XFGZFM8PC6
uses: [5W95QFHXPR, S1XK3HXHFX, 0ASGSTXSBW, HWPXM2JSJ9, M0Q5CFJ7ZH, ZA11N5XPZM, WA796ZCNRX, E5JXB0E324]
sources:
  - url: https://en.wikipedia.org/wiki/Plus_construction
---

## Definition

Let $X$ be a connected [[CW complex|5W95QFHXPR]] with a base point.
Let $P$ be a normal subgroup of the [[fundamental group|S1XK3HXHFX]] $\pi_1(X)$ that is [[perfect|HWPXM2JSJ9]], that is, $P$ equals its own [[commutator subgroup|0ASGSTXSBW]] $[P, P]$.
A *plus construction* of $X$ with respect to $P$ is a connected CW complex $X^+$ together with a map $f \colon X \to X^+$ such that:

1. The homomorphism $f_* \colon \pi_1(X) \to \pi_1(X^+)$ is surjective and its kernel is $P$.
2. For every $\pi_1(X^+)$-module $M$, the map $f$ induces isomorphisms $H_n(X; f^*M) \to H_n(X^+; M)$ in [[homology|M0Q5CFJ7ZH]] with local coefficients, for all $n \ge 0$.

## Remarks

A plus construction exists for every such pair $(X, P)$, and it is unique up to homotopy equivalence under $X$.
One builds it by attaching $2$-cells along loops that represent generators of $P$, and then $3$-cells that cancel the new classes in degree $2$.
The perfectness of $P$ is what makes the second step possible.
Every map $X \to Y$ that kills $P$ on $\pi_1$ factors through $X^+$, uniquely up to homotopy.

Example: let $R$ be a ring and $X = BGL(R)$, the [[classifying space|WA796ZCNRX]] of the discrete group $GL(R)$.
By Whitehead's lemma, the [[elementary subgroup|E5JXB0E324]] $E(R)$ is perfect and equals $[GL(R), GL(R)]$.
The plus construction for $P = E(R)$ gives $BGL(R)^+$, with $\pi_1(BGL(R)^+) = GL(R)/E(R) = K_1(R)$, and Quillen defines $K_n(R) = \pi_n(BGL(R)^+)$ for $n \ge 1$.

Non-example: take $X = S^1$ and $P = \pi_1(S^1) \cong \Z$, which is not perfect.
A map $f \colon S^1 \to Y$ with clause 1 makes $\pi_1(Y)$ trivial, so $H_1(Y; \Z) = 0$ by the [[Hurewicz theorem|ZA11N5XPZM]].
But $H_1(S^1; \Z) = \Z$, so clause 2 fails for $M = \Z$.
