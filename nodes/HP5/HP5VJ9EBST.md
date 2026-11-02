---
tag: HP5VJ9EBST
kind: concept
name: Fredholm minors
msc: [45B05]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_theory
---

## Summary

The Fredholm minors of a continuous kernel $K$ are entire functions of the parameter $\lambda$.
They are built like the [[Fredholm determinant|PPX0AK81QV]], from determinants of values of $K$, but with some rows and columns held at fixed points.
They are the integral analogues of the minors and cofactors of the matrix $I - \lambda A$.
The first minor divided by the Fredholm determinant is the [[resolvent kernel|ARTJV1XCRX]].
So the minors give the explicit solution of the [[Fredholm equation of the second kind|DEYYNVCV9J]].
At a zero of the determinant, the first minor that is not identically zero yields the solutions of the homogeneous equation.

## Explanations

### L1 human

For a square matrix, Cramer's rule writes the inverse as cofactors divided by the determinant.
Fredholm minors are the cofactors of an integral operator.
The first minor $D(x, y; \lambda)$ depends on two points $x$ and $y$, and $D(x, y; \lambda) / D(\lambda)$ is the kernel of the inverse operation.
For $K(x, y) = xy$ on $[0, 1]$ one finds $D(x, y; \lambda) = xy$, so the resolvent kernel is $xy / (1 - \lambda/3)$.
