---
tag: 7XFGVVTZ2X
kind: example
name: The 3 by 3 matrix with 4 on the diagonal and 1 elsewhere
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0G0RFPG8HR, 0VSSPAFM2C, 0FY42N02DV, 099TWVJ909, 03NDVCSHSB]
illustrates: [FWY8A9M5HK, 093X6MN6Y6, 0FRYPZ6D0X]
uses: [039HF58KQ5, 0AYEPBQMAW, 0S7A0EMPF4, 06YSJVR356, 0V58FPM3EQ, 0BNEXSKNRV, 0FRYPZ6D0X, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Three-dimensional matrix example
  - book: isbn:9780134860244
---

## Example

Let
$$A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}$$
over $\mathbb{R}$.
We find its characteristic polynomial, its eigenspaces, both multiplicities of each eigenvalue, and its minimal polynomial.

1. Write $A = 3I + J$, where $J$ has every entry $1$.
   Then $tI - A = (t - 3)I - J$, and the structure of $J$ will make every step short.
2. By the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]], we need the trace, the principal $2 \times 2$ minors and the determinant.
   The trace is $12$, each principal minor is $4 \cdot 4 - 1 \cdot 1 = 15$, so their sum is $45$, and
$$\det A = 4(16 - 1) - 1(4 - 1) + 1(1 - 4) = 60 - 3 - 3 = 54.$$
3. So the [[characteristic polynomial|039HF58KQ5]] is $p_A(t) = t^3 - 12t^2 + 45t - 54$.
4. It factors as $p_A(t) = (t - 3)^2 (t - 6)$.
   Check: $(t^2 - 6t + 9)(t - 6) = t^3 - 6t^2 - 6t^2 + 36t + 9t - 54 = t^3 - 12t^2 + 45t - 54$.
5. So the eigenvalue $3$ has [[algebraic multiplicity|0S7A0EMPF4]] $2$, and the eigenvalue $6$ has algebraic multiplicity $1$.
6. The matrix $A - 3I = J$ has three equal rows, so its rank is $1$.
   By the [[rank-nullity theorem|0W4FSW1TVB]], the [[eigenspace|0AYEPBQMAW]] $E_3 = \{ v : v_1 + v_2 + v_3 = 0 \}$ has dimension $2$, so the [[geometric multiplicity|06YSJVR356]] of $3$ is $2$.
7. Check on a basis of $E_3$:
$$A(1, -1, 0) = (3, -3, 0) = 3(1, -1, 0), \qquad A(1, 0, -1) = (3, 0, -3) = 3(1, 0, -1).$$
8. For $\lambda = 6$, each row of $A$ adds up to $6$, so $A(1, 1, 1) = (6, 6, 6) = 6(1, 1, 1)$, and $E_6$ is the line spanned by $(1, 1, 1)$.
9. Since every entry of $J^2$ is $1 + 1 + 1 = 3$, we have $J^2 = 3J$, and so
$$(A - 3I)(A - 6I) = J(J - 3I) = J^2 - 3J = 0.$$
10. The monic divisors of $(t - 3)(t - 6)$ of smaller degree are $1$, $t - 3$ and $t - 6$, and none annihilates $A$, since $I \ne 0$, $A - 3I = J \ne 0$ and $A - 6I = J - 3I \ne 0$.
11. So the [[minimal polynomial|0V58FPM3EQ]] is $m_A(t) = (t - 3)(t - 6) = t^2 - 9t + 18$, a proper divisor of $p_A$.

## Remarks

Each eigenvalue has equal algebraic and geometric multiplicity, so the eigenvectors $(1, -1, 0)$, $(1, 0, -1)$ and $(1, 1, 1)$ form a basis and $A$ is [[diagonalizable|07SQCNV233]].
This agrees with the fact that $m_A$ has no repeated root.
The eigenvectors for $3$ are orthogonal to $(1, 1, 1)$, as eigenvectors for distinct eigenvalues of a real symmetric matrix always are.

The same method works for every matrix $aI + bJ$ of size $n$ with $b \ne 0$.
The eigenvalue $a + nb$ belongs to $(1, \dots, 1)$, and the eigenvalue $a$ has the $(n - 1)$-dimensional eigenspace of vectors with entry sum $0$.
For $a = 3$, $b = 1$ and $n = 3$ this gives $6$ and $3$, as above.
If $b = 0$, then $A = aI$, and the minimal polynomial drops to $t - a$.

## Explanations

### L1 human

The matrix stretches the diagonal line through $(1, 1, 1)$ by the factor $6$.
It stretches every arrow in the plane $v_1 + v_2 + v_3 = 0$ by the factor $3$.
So one eigenvalue has a whole plane of eigenvectors, and together with the diagonal line they fill space.

### L2 human

The lesson is that a repeated root of $p_A$ can still come with a full eigenspace.
Here the root $3$ is double, and $E_3$ is a plane, so nothing is missing.
In the same way, the minimal polynomial needs the factor $t - 3$ only once.
Watch out: do not assume $m_A = p_A$ whenever $p_A$ has a repeated root; the [[shear|HTAWRAC3QE]] and this matrix both have repeated roots, and only the shear keeps the square in $m_A$.
