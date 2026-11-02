---
tag: 2YPJ39STQM
kind: statement
role: theorem
name: Cartan formula
msc: [55S10, 55N45]
uses: [VR7RHP41M0, EZYHSE1E8P, H7PCM776GR, JX47MS1R1H]
about: [VR7RHP41M0, EZYHSE1E8P]
sources:
  - url: https://en.wikipedia.org/wiki/Steenrod_algebra
---

## Statement

Let $X$ be a space, let $p$ be a prime, and let $x, y \in H^*(X; \F_p)$ be homogeneous classes, with $\abs{x}$ the degree of $x$.
Write $\smile$ for the [[cup product|JX47MS1R1H]].

1. For $p = 2$, the [[Steenrod squares|VR7RHP41M0]] satisfy, for every $k \ge 0$,
$$Sq^k(x \smile y) = \sum_{i + j = k} Sq^i x \smile Sq^j y.$$
2. For $p$ odd, the [[Steenrod reduced powers|EZYHSE1E8P]] satisfy, for every $k \ge 0$,
$$P^k(x \smile y) = \sum_{i + j = k} P^i x \smile P^j y.$$
3. For $p$ odd, the [[Bockstein homomorphism|H7PCM776GR]] $\beta$ of $0 \to \Z/p \to \Z/p^2 \to \Z/p \to 0$ is a derivation:
$$\beta(x \smile y) = \beta x \smile y + (-1)^{\abs{x}} x \smile \beta y.$$

## Remarks

The same formulas hold for the cross product $H^*(X) \otimes H^*(Y) \to H^*(X \times Y)$, and the cup product case follows by pulling back along the diagonal $X \to X \times X$.
The cross product case is checked in the construction of the operations, which are built from a product-compatible map on cochains.

In terms of the total square $Sq = \sum_{i \ge 0} Sq^i$, part 1 says that $Sq$ is a ring homomorphism of $H^*(X; \F_2)$.

Example: let $x$ generate $H^1(\R P^\infty; \F_2)$, so $H^*(\R P^\infty; \F_2) = \F_2[x]$.
Since $Sq^0 x = x$ and $Sq^1 x = x^2$, one has $Sq(x) = x + x^2$.
Then $Sq(x^n) = (x + x^2)^n$, so $Sq^i(x^n) = \binom{n}{i} x^{n+i}$.

## Explanations

### L1 human

The Cartan formula says how a Steenrod operation acts on a product of two classes.
The answer looks like the product rule for derivatives, with a sum over all ways to split the operation between the two factors.
It turns many computations of Steenrod operations into simple algebra.

### L2 human

With the Cartan formula and the values on degree-one or degree-two generators, one computes all Steenrod operations on the cohomology of $\R P^n$, $\C P^n$ and products of these.
It also gives the Hopf algebra structure of the Steenrod algebra: the coproduct sends $Sq^k$ to $\sum_{i+j=k} Sq^i \otimes Sq^j$.
Milnor used this coproduct to describe the dual of the Steenrod algebra.
