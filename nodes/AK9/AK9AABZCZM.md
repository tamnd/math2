---
tag: AK9AABZCZM
kind: example
name: The companion matrix of x² + 1
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
instance_of: [0ZCWPNZTQ3]
illustrates: [XYR7GPH20K]
uses: [0VH1TC1PWF, 039HF58KQ5, 03NDVCSHSB, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: lead section
---

## Example

Let $p = x^2 + 1$, so $n = 2$, $c_1 = 0$ and $c_0 = 1$.
By the [[definition|0VH1TC1PWF]], its companion matrix is
$$C = C(x^2 + 1) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$
We check its two polynomials and its eigenvalues over $\mathbb{R}$ and over $\mathbb{C}$.

1. Column $1$ is $e_2$, and column $2$ is $(-c_0, -c_1) = (-1, 0)$, as the definition requires.
2. The [[characteristic polynomial|039HF58KQ5]] is $\det \begin{pmatrix} x & 1 \\ -1 & x \end{pmatrix} = x^2 + 1 = p$.
3. Square the matrix: $C^2 = \begin{pmatrix} 0 \cdot 0 + (-1) \cdot 1 & 0 \cdot (-1) + (-1) \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot (-1) + 0 \cdot 0 \end{pmatrix} = -I$, so $C^2 + I = 0$.
4. $C$ is not a scalar matrix, so no monic polynomial of degree $1$ kills it. By step 3 the [[minimal polynomial|03NDVCSHSB]] is $m_C = x^2 + 1 = p$.
5. Over $\mathbb{R}$ the polynomial $x^2 + 1$ has no root, so $C$ has no real [[eigenvalue|0BQAA2BK3Q]]. Geometrically, $C$ turns the plane by a quarter turn, and no line through the origin stays in place.
6. Over $\mathbb{C}$ the eigenvalues are $i$ and $-i$. For example $C(1, -i) = (i, 1) = i \, (1, -i)$, and in the same way $C(1, i) = (-i, 1) = -i \, (1, i)$.

## Remarks

The polynomial fixes everything about $C(p)$, but the field decides whether $C(p)$ can be diagonalized.
Over $\mathbb{R}$ it cannot, since there are no eigenvalues, and over $\mathbb{C}$ it can, since the two eigenvalues $i$ and $-i$ are distinct.

Over a finite field the answer changes with the field.
Over $\mathbb{F}_2$ we have $x^2 + 1 = (x + 1)^2$ and $C = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which is similar to the Jordan block $J_2(1)$ and is not diagonalizable.
Over $\mathbb{F}_5$ we have $x^2 + 1 = (x - 2)(x - 3)$, and $C$ is similar to $\operatorname{diag}(2, 3)$.
Over $\mathbb{F}_3$ the polynomial has no root, since $0^2 + 1 = 1$, $1^2 + 1 = 2$ and $2^2 + 1 = 5 = 2$, so $C$ has no eigenvalue there.

## Explanations

### L1 human

The polynomial $x^2 + 1$ gives the matrix that turns the plane by a quarter turn.
Turning twice is the same as reflecting every point through the origin, so the square of the matrix is minus the identity.
That is the polynomial again: square plus one gives zero.
No real direction is kept by a quarter turn, so the matrix has no real eigenvalue.

### L2 human

Here is the diagonalization over $\mathbb{F}_5$.
First, $2^2 + 1 = 5 = 0$ and $3^2 + 1 = 10 = 0$, so $2$ and $3$ are the roots of $p$.
The kernel of $C - 2I = \begin{pmatrix} -2 & -1 \\ 1 & -2 \end{pmatrix}$ contains $(1, 3)$, since $-2 - 3 = -5 = 0$ and $1 - 6 = -5 = 0$.
The kernel of $C - 3I = \begin{pmatrix} -3 & -1 \\ 1 & -3 \end{pmatrix}$ contains $(1, 2)$, since $-3 - 2 = -5 = 0$ and $1 - 6 = -5 = 0$.
With $P$ the matrix with columns $(1, 3)$ and $(1, 2)$, we get $CP = P \operatorname{diag}(2, 3)$, and $\det P = 2 - 3 = -1 \ne 0$.
So a companion matrix is diagonalizable over a field exactly when its polynomial has distinct roots in that field, and the trap is to say "not diagonalizable" without naming the field.
