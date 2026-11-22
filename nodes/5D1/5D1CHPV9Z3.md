---
tag: 5D1CHPV9Z3
kind: statement
role: proposition
name: A family of n vectors is a basis if and only if its determinant is nonzero
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
uses: [0V94H674MB, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Statement

One determinant decides whether $n$ vectors in an $n$-dimensional space form a basis.
Let $F$ be a field, let $V$ be a vector space over $F$ of dimension $n \ge 1$, and let $B$ be a basis of $V$.
Then vectors $v_1, \dots, v_n \in V$ form a [[basis|0VTQTPQGAV]] of $V$ if and only if
$$\det_B(v_1, \dots, v_n) \ne 0,$$
where $\det_B$ is the [[determinant in the basis $B$|0V94H674MB]].

## Remarks

### A quick test

Do $(1, 2, 0)$, $(0, 1, 1)$ and $(1, 0, 1)$ form a basis of $\mathbb{R}^3$?
Put them as columns and expand along the first row:
$$\det \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} = 1 \cdot (1 - 0) - 0 + 1 \cdot (2 - 0) = 3.$$
The value is $3 \ne 0$, so they form a basis, and no system of equations had to be solved.

### Why each hypothesis is needed

The family must have exactly $n = \dim V$ vectors, since otherwise $\det_B$ is not defined; for fewer or more vectors, the rank of the coordinate matrix answers the question instead.

The scalars must form a field.
Over $\mathbb{Z}$, the family $(2)$ in $\mathbb{Z}^1$ has determinant $2 \ne 0$, but it is not a basis, because $1$ is not an integer multiple of $2$.
Over a commutative ring, the correct condition is that $\det_B(v_1, \dots, v_n)$ is a unit, and in a field the units are exactly the nonzero elements.

### What it gives you

Taking the negation of both sides, the vectors are linearly dependent if and only if $\det_B(v_1, \dots, v_n) = 0$.
The answer depends on the field, not only on the numbers.
For example, the polynomials $1 + x$, $x + x^2$, $1 + x^2$ have determinant $2$ in the basis $1, x, x^2$, so [[they form a basis over $\mathbb{Q}$ but not over $\mathbb{F}_2$|XNG0N654EM]].
Since the [[change of basis rule|T1WN2DHS63]] multiplies $\det_B$ by a nonzero factor, the test gives the same answer for every choice of $B$.

### The converse

The statement is an equivalence, so both directions hold: a basis has a nonzero determinant, and a nonzero determinant gives a basis.
The [[proof|19WJK6SSM8]] proves both at once through the coordinate map.

## Explanations

### L1 human

Take $n$ vectors in a space of dimension $n$.
Write their coordinates as the columns of a square matrix.
The vectors form a basis exactly when the determinant of this matrix is not zero.
For the plane, $(1, 2)$ and $(2, 4)$ give $1 \cdot 4 - 2 \cdot 2 = 0$, and indeed the second vector is twice the first.

### L2 human

Here is a typical use: for which numbers $t$ do $(1, t)$ and $(t, 4)$ form a basis of $\mathbb{R}^2$?
The determinant is
$$\det \begin{pmatrix} 1 & t \\ t & 4 \end{pmatrix} = 4 - t^2.$$
It vanishes exactly for $t = 2$ and $t = -2$.
So the two vectors form a basis for every $t$ except $\pm 2$.
Check: for $t = 2$ the vectors are $(1, 2)$ and $(2, 4)$, and the second is twice the first.
Watch out: the test needs exactly $n$ vectors, and three vectors in the plane are never a basis, whatever numbers you try.

### L3 human

The statement is the [[invertibility criterion|FBSAPTP1PR]] for the coordinate matrix, carried over to $V$ by the coordinate isomorphism $V \to F^n$.
Over a commutative ring $K$, the same argument shows that $n$ vectors form a basis of a free module of rank $n$ if and only if their determinant is a unit of $K$.
