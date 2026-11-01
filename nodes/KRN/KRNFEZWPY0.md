---
tag: KRNFEZWPY0
kind: concept
name: Field norm
msc: [12F05, 11R04]
sources:
  - url: https://en.wikipedia.org/wiki/Field_norm
same_as:
  wikidata: Q1999258
  wikipedia: Field norm
---

## Summary

Let $L/K$ be a [[finite extension|0C1Y04SZ1W]] and let $\alpha \in L$.
Multiplication by $\alpha$ is a $K$-linear map of $L$, and the field norm $N_{L/K}(\alpha)$ is its [[determinant|0X0HQYSZ0K]].
It is a multiplicative map $L \to K$, and it is nonzero exactly on the nonzero elements.
For a separable extension it is the product of the images of $\alpha$ under all embeddings of $L$ into an algebraic closure.
Norms measure the size of algebraic numbers, detect units in rings of integers, and appear in [[Hilbert's Theorem 90|YFF8B5A0QG]].

## Explanations

### L1 human

Multiplying by a fixed element $\alpha$ stretches the field $L$, seen as a vector space over $K$.
The norm is the determinant of this stretching.
For the Gaussian numbers $a + bi$ over $\Q$, it is $a^2 + b^2$, the product of $a + bi$ and its conjugate $a - bi$.
So $N(3 + 4i) = 25$.
The rule $N(\alpha\beta) = N(\alpha) N(\beta)$ explains why a product of sums of two squares is again a sum of two squares.
