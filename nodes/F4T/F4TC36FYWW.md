---
tag: F4TC36FYWW
kind: example
name: Change of basis to Taylor coordinates for quadratic polynomials
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0MKRHZB3WS]
uses: [0KWXYZPJKN, 0BMVBHTWV2, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Change-of-basis formula
  - book: isbn:9780134860244
    locator: Section 2.5
---

## Example

Rewriting a polynomial in powers of $x - 1$ is a change of basis, and its matrix is upper triangular.
Let $V$ be the space of real polynomials of degree at most $2$, with the bases $B = (1, x, x^2)$ and $B' = (1, x - 1, (x - 1)^2)$.

1. We expand each new basis vector in the old basis:
   $$1 = 1, \qquad x - 1 = -1 + x, \qquad (x - 1)^2 = 1 - 2x + x^2.$$
2. By the [[definition|0KWXYZPJKN]], the coefficient lists $(1, 0, 0)$, $(-1, 1, 0)$ and $(1, -2, 1)$ are the columns of the change of basis matrix from $B$ to $B'$:
   $$P = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}.$$
3. For the inverse we expand each old basis vector in the new basis, using $x = 1 + (x - 1)$:
   $$1 = 1, \qquad x = 1 + (x - 1), \qquad x^2 = 1 + 2(x - 1) + (x - 1)^2.$$
   So
   $$P^{-1} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}.$$
4. We check $PP^{-1} = I_3$ with the [[matrix product|076JGP6R3T]].
   Row 1 of $P$ times columns 2 and 3 of $P^{-1}$ gives $1 - 1 = 0$ and $1 - 2 + 1 = 0$.
   Row 2 times column 3 gives $2 - 2 = 0$, and the diagonal entries are $1$.
5. Let $p = 2 - x + 3x^2$, with [[coordinates|0BMVBHTWV2]] $[p]_B = (2, -1, 3)$.
   The new coordinates are
   $$[p]_{B'} = P^{-1} \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 - 1 + 3 \\ -1 + 6 \\ 3 \end{pmatrix} = \begin{pmatrix} 4 \\ 5 \\ 3 \end{pmatrix}.$$
6. Check: $4 + 5(x - 1) + 3(x - 1)^2 = 4 + 5x - 5 + 3x^2 - 6x + 3 = 2 - x + 3x^2$.

## Remarks

For a general $p = a + bx + cx^2$, the same product gives $[p]_{B'} = (a + b + c,\ b + 2c,\ c)$.
These three numbers are $p(1)$, $p'(1)$ and $p''(1)/2$, so the new coordinates are the Taylor coefficients of $p$ at $1$.
For $p = 2 - x + 3x^2$ we get $p(1) = 4$, $p'(1) = -1 + 6 = 5$ and $p''(1)/2 = 3$, as in step 5.

Both matrices are upper triangular with ones on the diagonal, because each new basis vector $(x - 1)^k$ has leading term $x^k$.
If we expand around a point $a$ in place of $1$, then $P$ has the entries $-a$, $a^2$ and $-2a$ in place of $-1$, $1$ and $-2$, and $P^{-1}$ is the same matrix with $a$ replaced by $-a$.

## Explanations

### L1 human

Changing to the basis of powers of $x - 1$ rewrites a polynomial around the point $1$ in place of the point $0$.
The change of basis matrix collects the expansions of $1$, $x - 1$ and $(x - 1)^2$.
Its inverse collects the expansions of $1$, $x$ and $x^2$ in powers of $x - 1$, and it is the matrix you multiply by to get the new coefficients.

### L2 human

The example shows that a change of basis need not involve vectors in $\mathbb{R}^n$ at all: the coordinates live in $\mathbb{R}^3$, but the vectors are polynomials.
Watch out: the matrix $P$ is built from the new basis, but the new coordinates come from $P^{-1}$.
Applying $P$ to $(2, -1, 3)$ gives $(6, -7, 3)$, and $6 - 7(x - 1) + 3(x - 1)^2 = 16 - 13x + 3x^2$, which is not $p$.
