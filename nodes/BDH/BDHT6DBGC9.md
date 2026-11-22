---
tag: BDHT6DBGC9
kind: example
name: The adjugate and the inverse of a 3 × 3 matrix
msc: ["15A09"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [07W9H8QF38]
uses: [0GMPYM0NSR, 0528HKWZ1Z, 0ENVM493VK]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: 3 × 3 numeric matrix
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$$
over $\mathbb{Q}$.
We compute its adjugate, check the adjugate identity, and read off the inverse.

1. Expansion along row $1$ gives
$$\det A = 1 (50 - 48) - 2 (40 - 42) + 3 (32 - 35) = 2 + 4 - 9 = -3.$$
2. The nine cofactors, computed in the [[cofactor example|CS8M5BY36A]], form the cofactor matrix
$$C = \begin{pmatrix} 2 & 2 & -3 \\ 4 & -11 & 6 \\ -3 & 6 & -3 \end{pmatrix}.$$
   For instance, $C_{21} = -(2 \cdot 10 - 3 \cdot 8) = 4$ and $C_{22} = 1 \cdot 10 - 3 \cdot 7 = -11$.
3. By the [[definition of the adjugate|0GMPYM0NSR]], the adjugate is the transpose of $C$:
$$\operatorname{adj} A = C^{\mathsf{T}} = \begin{pmatrix} 2 & 4 & -3 \\ 2 & -11 & 6 \\ -3 & 6 & -3 \end{pmatrix}.$$
4. Row $1$ of $A$ times the three columns of $\operatorname{adj} A$ gives $2 + 4 - 9 = -3$, then $4 - 22 + 18 = 0$, then $-3 + 12 - 9 = 0$.
5. Row $2$ gives $8 + 10 - 18 = 0$, then $16 - 55 + 36 = -3$, then $-12 + 30 - 18 = 0$.
6. Row $3$ gives $14 + 16 - 30 = 0$, then $28 - 88 + 60 = 0$, then $-21 + 48 - 30 = -3$.
7. So $A \operatorname{adj} A = -3 I_3$, as the [[adjugate identity|0528HKWZ1Z]] predicts.
8. Since $-3$ is a unit of $\mathbb{Q}$, the [[inverse via the adjugate|0ENVM493VK]] gives
$$A^{-1} = -\frac{1}{3} \operatorname{adj} A = \begin{pmatrix} -2/3 & -4/3 & 1 \\ -2/3 & 11/3 & -2 \\ 1 & -2 & 1 \end{pmatrix}.$$

## Remarks

Steps 4 to 6 are an independent check of the whole computation.
A single wrong cofactor would put a nonzero entry off the diagonal or a wrong value on it, so the check is worth its cost.

The denominators $3$ in $A^{-1}$ come from $\det A = -3$.
Over $\mathbb{Z}$ the matrix $A$ has no inverse, because $-3$ is not a unit of $\mathbb{Z}$, even though $\operatorname{adj} A$ has integer entries.
The determinant is linear in the corner entry, with coefficient $C_{33} = -3$.
So if we change that entry from $10$ to $9$, the determinant changes by $(-1) \cdot (-3) = 3$, and it becomes $0$.
The new matrix is the [[singular example|H98NXA00NZ]], whose adjugate has rank $1$ and gives no inverse.

## Explanations

### L1 human

The adjugate is built from nine small determinants, one for each entry, with signs, and then flipped across the diagonal.
Multiplying $A$ by its adjugate gives $-3$ times the identity matrix.
So dividing the adjugate by $-3$ gives the inverse of $A$.

### L2 human

The product $A \operatorname{adj} A$ is the best test of a hand-computed adjugate: every entry off the diagonal must be $0$, and every diagonal entry must be $\det A$.
For example, if we forget the transpose in step 3 and use $C$ itself, then row $1$ of $A$ times column $2$ of $C$ is $2 - 22 + 18 = -2$, not $0$.
The [[non-example on the missing transpose|2BJC4DHCMK]] carries this out in full.
