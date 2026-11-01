---
tag: KQ7V0J5CGG
kind: concept
name: Matrix pencil
msc: [15A22]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_pencil
same_as:
  wikidata: Q3739929
  wikipedia: Matrix pencil
---

## Summary

A matrix pencil is a family of matrices $A - \lambda B$ that depends linearly on a parameter $\lambda$.
Its eigenvalues are the values of $\lambda$ for which $A - \lambda B$ is singular, which leads to the generalised eigenvalue problem $Av = \lambda Bv$.
Pencils arise in vibration problems, in differential-algebraic equations and in control theory, and they are classified by the Kronecker canonical form.
More general pencils allow higher powers of $\lambda$; the linear ones are the most common.

## Explanations

### L1 human

Take two matrices $A$ and $B$ of the same size and look at all the combinations $A - \lambda B$ as the number $\lambda$ varies.
The ordinary eigenvalue problem is the case $B = I$.
In mechanics, $A$ may describe stiffness and $B$ mass, and the eigenvalues of the pencil give the squares of the natural frequencies.
For $A = \operatorname{diag}(1, 2)$ and $B = I$, the matrix $A - \lambda B$ is singular exactly for $\lambda = 1$ and $\lambda = 2$.
