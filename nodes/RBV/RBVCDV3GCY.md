---
tag: RBVCDV3GCY
kind: definition
name: Eigenvalue algorithm
msc: [65F15, 15A18]
defines: HCJ2ETX89Z
uses: [0VD9ZSWWJG, 0BQAA2BK3Q, 0N6960W0BV]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalue_algorithm
---

## Definition

Let $n \ge 1$ and let $\mathbb{K}$ be $\R$ or $\C$.
An *eigenvalue algorithm* is an algorithm that takes as input a [[matrix|0VD9ZSWWJG]] $A \in \mathbb{K}^{n \times n}$ (and, for iterative algorithms, a tolerance $\varepsilon > 0$) and returns:

1. numbers $\tilde\lambda_1, \dots, \tilde\lambda_k \in \C$, with $1 \le k \le n$, that approximate [[eigenvalues|0BQAA2BK3Q]] $\lambda_1, \dots, \lambda_k$ of $A$, counted with algebraic multiplicity, to within the tolerance;
2. optionally, vectors $\tilde v_1, \dots, \tilde v_k$ that approximate corresponding [[eigenvectors|0N6960W0BV]] or bases of invariant subspaces.

It computes *all* eigenvalues when $k = n$, and *some* eigenvalues otherwise, for example those of largest modulus or those closest to a given shift.

## Remarks

Example: the [[QR algorithm|B6F8YWHYZ5]] reduces $A$ to Hessenberg form and applies shifted QR steps until the matrix is nearly upper triangular.
Its diagonal then approximates all $n$ eigenvalues, so it is an eigenvalue algorithm with $k = n$.
Non-example: an algorithm that only computes the coefficients of the [[characteristic polynomial|0VSSPAFM2C]] does not return eigenvalues, so clause 1 fails.
Finding the roots is a further step, and it is badly conditioned in general.
The eigenvalues of a general matrix with $n \ge 5$ are not expressible by radicals in its entries.
So every eigenvalue algorithm that works for all such matrices is iterative and stops at a tolerance.
Accuracy is usually measured by backward error: the output should be the exact eigenvalues of a matrix $A + E$ with $\norm{E}$ small compared with $\norm{A}$.

## Explanations

### L1 human

An eigenvalue algorithm is any recipe that, given a square matrix, outputs its eigenvalues (and maybe eigenvectors) up to a chosen accuracy.
Some recipes find all of them, others find only a few that one asks for.
