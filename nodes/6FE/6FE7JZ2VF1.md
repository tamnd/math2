---
tag: 6FE7JZ2VF1
kind: object
name: Calkin algebra
msc: [46L05, 47L30, 47A53]
uses: [HM2HHE3J51, BMDG4JQPEH, 2WAZF1RV2Y, M2NEP1K5AE, 9240K052CS]
sources:
  - url: https://en.wikipedia.org/wiki/Calkin_algebra
same_as:
  wikidata: Q1027067
  wikipedia: Calkin algebra
---

## Description

Let $H$ be an infinite-dimensional separable complex [[Hilbert space|HM2HHE3J51]].
Let $B(H)$ be the [[algebra of bounded operators|BMDG4JQPEH]] on $H$, and let $K(H)$ be the [[ideal of compact operators|2WAZF1RV2Y]] in it.
The *Calkin algebra* of $H$ is the [[quotient|9240K052CS]] $Q(H) = B(H) / K(H)$.
It carries the quotient norm and the induced product.
Its involution is $\pi(T)^* = \pi(T^*)$, where $\pi \colon B(H) \to Q(H)$ is the quotient map.

## Remarks

Since $K(H)$ is a closed two-sided ideal of $B(H)$ that is closed under adjoints, $Q(H)$ is a unital C*-algebra.
Calkin showed that for separable $H$, $K(H)$ is the only closed two-sided ideal of $B(H)$ other than $\set{0}$ and $B(H)$, so $Q(H)$ is a simple C*-algebra.
An operator $T \in B(H)$ is Fredholm exactly when $\pi(T)$ is invertible in $Q(H)$.
The spectrum of $\pi(T)$ in $Q(H)$ is the essential spectrum of $T$.
The algebra $Q(H)$ is infinite-dimensional and not separable as a normed space.
The construction makes sense for any Hilbert space, but for non-separable $H$ the ideal $K(H)$ is no longer the only nontrivial closed ideal.

## Explanations

### L1 human

The Calkin algebra is what remains of the bounded operators when compact operators are treated as zero.
Two operators are the same element of it when they differ by a compact operator, a small error in a precise sense.
In this algebra, the right shift on sequences becomes invertible, since it has an inverse up to a rank-one error.
It is the natural home of the Fredholm index and of the essential spectrum.
