---
tag: 0TYMASG33Y
kind: statement
role: proposition
name: Characteristic polynomial does not depend on the basis
msc: [15A15, 15A18]
uses: [039HF58KQ5, 027KDW2K72]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Statement

Let $K$ be a commutative ring, let $A$ be an $n \times n$ matrix over $K$, and let $P$ be an invertible $n \times n$ matrix over $K$.
Then the [[characteristic polynomials|0VSSPAFM2C]] of $A$ and $P^{-1} A P$ are equal:
$$p_{P^{-1} A P}(t) = p_A(t).$$
So [[similar matrices|0E89HQATM8]] have the same characteristic polynomial.

## Remarks

The proof is $\det(t I - P^{-1} A P) = \det(P^{-1} (t I - A) P) = \det(t I - A)$.
Hence the characteristic polynomial of a linear map does not depend on the basis.
The converse fails: $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ both have $p(t) = (t - 1)^2$, but they are not similar.

## Explanations

### L1 human

A change of basis does not change the characteristic polynomial.
So the eigenvalues, the trace and the determinant, which we can read from it, are the same in every basis.
They are properties of the linear map, not of one matrix.
