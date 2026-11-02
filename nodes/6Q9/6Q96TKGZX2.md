---
tag: 6Q96TKGZX2
kind: definition
name: Monoid ring
msc: [16S36, 20M25, 16S34]
defines: 1HM7ZYMPD7
uses: [0N6R902FG1, 0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Monoid_ring
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $M$ be a [[monoid|0N6R902FG1]], written multiplicatively with identity $e$.
The *monoid ring* $R[M]$ is the set of functions $f \colon M \to R$ with $f(m) \ne 0$ for only finitely many $m \in M$.
Such a function is written as a finite formal sum $\sum_{m \in M} f(m) \, m$.
Addition is pointwise, and multiplication is the convolution
$$(f g)(m) = \sum_{\substack{x, y \in M \\ x y = m}} f(x) \, g(y).$$
The sum is finite because $f$ and $g$ have finite support.
With these operations $R[M]$ is a ring with identity $1 \cdot e$.

## Remarks

Example: for the monoid $M = \set{1, x, x^2, \dots}$ with $x^i x^j = x^{i+j}$, the convolution is the usual product of polynomials, so $R[M]$ is the [[polynomial ring|0SDC934R52]] $R[x]$.
For instance $(1 + x)(1 - x) = 1 \cdot 1 + (1 - 1) x - x^2 = 1 - x^2$.
For a [[group|G5S1M9]] $G$, $R[G]$ is the [[group ring|4NMTSX0XDS]], and for $M = (\Z, +)$ it is the [[Laurent polynomial ring|QMY5JTZZB8]].
Non-example: the set of all functions $\Z \to R$ with the same product is not a ring, because the finiteness condition fails and the convolution sum $\sum_{i + j = n} f(i) g(j)$ can be an infinite sum.
The ring $R[M]$ is commutative when $R$ and $M$ are commutative.
When $R$ is commutative, each monoid homomorphism from $M$ to the multiplicative monoid of an $R$-algebra $A$ extends uniquely to an $R$-algebra homomorphism $R[M] \to A$.
In additive notation for $M$, the same ring is often called the monoid algebra.
