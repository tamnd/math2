---
tag: 18XQY67HMS
kind: example
name: A 3 by 3 matrix with a defective eigenvalue
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
instance_of: [7JJE96MZQY, 099TWVJ909, 03NDVCSHSB]
illustrates: [093X6MN6Y6, 0QF4ZEFG52, FWY8A9M5HK]
uses: [039HF58KQ5, 0FRYPZ6D0X, 06YSJVR356, 0S7A0EMPF4, 0V58FPM3EQ, 0BNEXSKNRV, 0F765KFC2J, 0VTAD25A3G, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Example
  - book: isbn:9780134860244
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 & 0 \\ -1 & 3 & 0 \\ -1 & 1 & 1 \end{pmatrix}$$
over $\mathbb{R}$.
We find its eigenvalues, the two multiplicities of each, and its minimal polynomial.

1. Expand $\det(tI - A)$ along the third column, whose only nonzero entry is $t - 1$ in the corner:
$$p_A(t) = (t - 1)\big((t - 1)(t - 3) + 1\big) = (t - 1)(t^2 - 4t + 4) = (t - 1)(t - 2)^2.$$
2. Check with the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]].
   The trace is $1 + 3 + 1 = 5$, the principal $2 \times 2$ minors are $1 \cdot 3 - 1 \cdot (-1) = 4$, $1 \cdot 1 - 0 = 1$ and $3 \cdot 1 - 0 = 3$, with sum $8$, and $\det A = 4$.
   So $p_A(t) = t^3 - 5t^2 + 8t - 4$, and multiplying out $(t - 1)(t - 2)^2$ gives the same polynomial.
3. For the eigenvalue $1$, the vector $(0, 0, 1)$ works, since $A(0, 0, 1) = (0, 0, 1)$.
4. For the eigenvalue $2$, the vector $(1, 1, 0)$ works:
$$A(1, 1, 0) = (1 + 1,\ -1 + 3,\ -1 + 1) = (2, 2, 0) = 2(1, 1, 0).$$
5. The matrix
$$A - 2I = \begin{pmatrix} -1 & 1 & 0 \\ -1 & 1 & 0 \\ -1 & 1 & -1 \end{pmatrix}$$
   has two equal rows and a third row that is not a multiple of them, so its rank is $2$.
   By the [[rank-nullity theorem|0W4FSW1TVB]] the [[geometric multiplicity|06YSJVR356]] of $2$ is $3 - 2 = 1$, while its [[algebraic multiplicity|0S7A0EMPF4]] is $2$.
6. The matrix $A - I$ has the rows $(0, 1, 0)$, $(-1, 2, 0)$ and $(-1, 1, 0)$, of rank $2$, so the geometric multiplicity of $1$ is $1$.
7. Multiply the two linear factors:
$$(A - I)(A - 2I) = \begin{pmatrix} -1 & 1 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \ne 0.$$
8. Square the factor for $2$:
$$(A - 2I)^2 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & -1 & 1 \end{pmatrix} \ne 0.$$
9. Every proper monic divisor of $p_A$ divides $(t - 1)(t - 2)$ or $(t - 2)^2$.
   If a divisor annihilated $A$, so would these multiples of it, and steps 7 and 8 show that they do not.
10. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $p_A(A) = 0$.
    Since the [[minimal polynomial divides every annihilating polynomial|0VTAD25A3G]], the [[minimal polynomial|0V58FPM3EQ]] is a monic divisor of $p_A$, and by step 9 it is $p_A$ itself:
$$m_A(t) = (t - 1)(t - 2)^2.$$

## Remarks

The eigenvalue $2$ is defective: it is a double root, but it has only the line of eigenvectors spanned by $(1, 1, 0)$.
With the line for $1$, the eigenvectors span only a plane, so $A$ is not [[diagonalizable|07SQCNV233]].
The squared factor $(t - 2)^2$ in $m_A$ shows the same failure, because a matrix is diagonalizable exactly when its minimal polynomial has no repeated root.

The Jordan form makes the picture explicit.
With $P = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ and $J = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ we have $AP = PJ$.
Check on the second column: $A(0, 1, 1) = (1, 3, 2)$, which equals $(1, 1, 0) + 2(0, 1, 1)$.
Change the entry in place $(3, 1)$ from $-1$ to $0$ and $p_A$ stays the same, but now $A - 2I$ has the rows $(-1, 1, 0)$, $(-1, 1, 0)$ and $(0, 1, -1)$, still of rank $2$, so the defect remains.

## Explanations

### L1 human

The number $2$ is a double root of the characteristic polynomial of this matrix.
You might expect two independent directions that the matrix stretches by $2$.
There is only one, the line through $(1, 1, 0)$.
So the matrix has too few eigenvectors, and no change of basis can make it diagonal.

### L2 human

The typical use is to find $m_A$ by testing divisors of $p_A$.
A minimal polynomial must contain each linear factor $t - \lambda$ at least once, so the only candidates of degree $2$ are $(t - 1)(t - 2)$ and $(t - 2)^2$.
Both fail, by steps 7 and 8, so $m_A = p_A$.
Watch out: the product in step 7 has a zero row, and it is tempting to stop there, but a matrix with a zero row is not the zero matrix.
