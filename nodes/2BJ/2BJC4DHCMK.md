---
tag: 2BJC4DHCMK
kind: example
name: The cofactor matrix without the transpose is not the adjugate
msc: ["15A09"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [0XPKR18APA]
not_instance_of:
  - target: 07W9H8QF38
    note: the cofactor matrix C of A is not adj A, since A C has the entry -2 off the diagonal while A adj A is -3 times the identity
uses: [0GMPYM0NSR, 0528HKWZ1Z, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Definition
---

## Example

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$ and $C = \begin{pmatrix} 2 & 2 & -3 \\ 4 & -11 & 6 \\ -3 & 6 & -3 \end{pmatrix}$, its cofactor matrix.

1. The [[matrix product|076JGP6R3T]] $AC$ has row $1$ equal to $(2 + 8 - 9, 2 - 22 + 18, -3 + 12 - 9) = (1, -2, 0)$.
2. In full, $AC = \begin{pmatrix} 1 & -2 & 0 \\ 10 & -11 & 0 \\ 16 & -14 & -3 \end{pmatrix}$.
3. This is not a multiple of $I_3$. By the [[adjugate identity|0528HKWZ1Z]], $A \operatorname{adj} A = -3 I_3$, so $C \neq \operatorname{adj} A$.
4. The transpose $C^{T}$ is the [[adjugate|0GMPYM0NSR]], and it passes the test.

## Remarks

For a symmetric $A$ the cofactor matrix is symmetric, so $C = C^{T}$ and the error makes no difference.
The cofactor matrix can also be symmetric for a matrix that is not symmetric, as for the matrix $S$ of the [[singular example|H98NXA00NZ]].

## Explanations

### L1 human

The adjugate needs one more step after the cofactors: flip them across the diagonal.
Without that step, the product with $A$ is not a multiple of the identity.

### L2 human

The test $A \operatorname{adj} A = (\det A) I_n$ finds this error at once.
A trap: tests on symmetric matrices do not find a missing transpose.
