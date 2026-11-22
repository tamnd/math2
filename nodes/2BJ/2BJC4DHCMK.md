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

Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}, \qquad C = \begin{pmatrix} 2 & 2 & -3 \\ 4 & -11 & 6 \\ -3 & 6 & -3 \end{pmatrix},$$
where $C$ is the cofactor matrix of $A$ from the [[worked example|CS8M5BY36A]] and $\det A = -3$.
We show that $C$ itself is not the [[adjugate|0GMPYM0NSR]], although its transpose is.

1. The [[adjugate identity|0528HKWZ1Z]] says that $A \operatorname{adj} A = (\det A) I_3 = -3 I_3$.
   So any candidate for $\operatorname{adj} A$ must give $-3 I_3$ when multiplied by $A$.
2. Compute the first row of the [[matrix product|076JGP6R3T]] $AC$, using the row $(1, 2, 3)$ and the three columns of $C$:
$$(2 + 8 - 9, \ 2 - 22 + 18, \ -3 + 12 - 9) = (1, -2, 0).$$
3. The other two rows are found in the same way, and
$$AC = \begin{pmatrix} 1 & -2 & 0 \\ 10 & -11 & 0 \\ 16 & -14 & -3 \end{pmatrix}.$$
4. This matrix has nonzero entries off the diagonal, so it is not $-3 I_3$, and $C \neq \operatorname{adj} A$.
5. Now use the transpose.
   The first row of $A C^{\mathsf{T}}$ pairs $(1, 2, 3)$ with the rows of $C$:
$$(2 + 4 - 9, \ 4 - 22 + 18, \ -3 + 12 - 9) = (-3, 0, 0).$$
   The other rows work in the same way, and $A C^{\mathsf{T}} = -3 I_3$, so $C^{\mathsf{T}}$ passes the test.

## Remarks

The reason for the transpose is that the identity pairs row $i$ of $A$ with the cofactors of row $i$, and a matrix product pairs a row with a column.
So the cofactors of row $i$ must sit in column $i$, which is what the transpose does.

For a symmetric matrix the cofactor matrix is also symmetric, so $C = C^{\mathsf{T}}$, and forgetting the transpose does no harm.
The cofactor matrix can also be symmetric when $A$ is not, as for the matrix with rows $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 9)$ in the [[singular example|H98NXA00NZ]].
So a test on such a matrix does not catch the error, and the matrix of this example, with $10$ in the corner, is a better test case.

## Explanations

### L1 human

The adjugate needs one more step after the cofactors: flip the table across its main diagonal.
Without that step, the product with $A$ is not the identity times the determinant.
Here the product has a $-2$ where a $0$ should be.

### L2 human

The test $A \operatorname{adj} A = (\det A) I_n$ finds a missing transpose at once, and one row of the product is often enough.
Here row $1$ of $AC$ is $(1, -2, 0)$, while row $1$ of $AC^{\mathsf{T}}$ is $(-3, 0, 0)$ as it should be.
Watch out: tests on symmetric matrices cannot find this error, because for them the transpose changes nothing.
