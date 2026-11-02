---
tag: A3AP0P0D4M
kind: statement
role: theorem
name: Hopf invariant one problem
msc: [55Q25, 55Q40]
uses: [TEGTSY7XMX, P976WYEFMB]
about: [TEGTSY7XMX]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_invariant
---

## Statement

Let $n \ge 2$.
There is a continuous map $f \colon S^{2n-1} \to S^n$ with [[Hopf invariant|TEGTSY7XMX]] $H(f) = \pm 1$ if and only if $n \in \set{2, 4, 8}$.

## Remarks

The maps for $n = 2, 4, 8$ are the Hopf fibrations built from the complex numbers, the quaternions and the octonions.
For odd $n$, every Hopf invariant is $0$, and for even $n$, the Whitehead product $[\iota_n, \iota_n]$ has Hopf invariant $\pm 2$, so only the value $\pm 1$ is in question.
An argument with Steenrod squares shows that $n$ must be a power of $2$.
J. F. Adams excluded all remaining $n \ge 16$ with secondary cohomology operations, which is [[Adams' theorem on Hopf invariant one|ZJVKZ8D64P]].
Adams and Atiyah later gave a short proof with Adams operations in topological K-theory.
Consequences: $\R^n$ carries the structure of a real division algebra, with a bilinear product and no zero divisors, only for $n = 1, 2, 4, 8$, and $S^{n-1}$ is an H-space only for $n = 1, 2, 4, 8$.

## Explanations

### L1 human

The Hopf map wraps the $3$-sphere around the $2$-sphere with the simplest possible twist, measured by Hopf invariant one.
The question is in which dimensions such a simplest twist exists.
The answer is only in dimensions $2$, $4$ and $8$, the dimensions of the complex numbers, the quaternions and the octonions.

### L2 human

The theorem explains why the list $\R, \C, \mathbb{H}, \mathbb{O}$ of division algebras stops.
A bilinear product without zero divisors on $\R^n$ makes $S^{n-1}$ an H-space, and the Hopf construction turns this multiplication into a map $S^{2n-1} \to S^n$ of Hopf invariant $\pm 1$.
So the topological theorem implies the algebraic one.
The problem also led to the Adams spectral sequence and to the use of K-theory operations in homotopy theory.
