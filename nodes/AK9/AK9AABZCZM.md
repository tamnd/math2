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

1. Column $1$ is $e_2$ and column $2$ is $(-c_0, -c_1) = (-1, 0)$, as the definition requires.
2. [[Characteristic polynomial|039HF58KQ5]]: $\det \begin{pmatrix} x & 1 \\ -1 & x \end{pmatrix} = x^2 + 1 = p$.
3. $C^2 = \begin{pmatrix} 0 \cdot 0 + (-1) \cdot 1 & 0 \\ 0 & 1 \cdot (-1) + 0 \end{pmatrix} = -I$. So $C^2 + I = 0$.
4. [[Minimal polynomial|03NDVCSHSB]]: $C$ is not a scalar matrix, so no monic polynomial of degree $1$ kills it. By step 3, $m_C = x^2 + 1 = p$.
5. Over $\mathbb{R}$, $x^2 + 1$ has no root, so $C$ has no real [[eigenvalue|0BQAA2BK3Q]]. Geometrically, $C$ is the rotation of the plane by a quarter turn.
6. Over $\mathbb{C}$, $C$ has the eigenvalues $i$ and $-i$, with eigenvectors $(1, -i)$ and $(1, i)$: $C(1, -i) = (i, 1) = i\,(1, -i)$.

## Remarks

The example shows that the polynomial decides everything about $C(p)$, and that the field decides whether $C(p)$ can be diagonalized.
Over $\mathbb{F}_2$, $x^2 + 1 = (x + 1)^2$, and $C = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is similar to the Jordan block $J_2(1)$, not diagonalizable.
Over $\mathbb{F}_5$, $x^2 + 1 = (x - 2)(x - 3)$, and $C$ is similar to $\operatorname{diag}(2, 3)$.

## Explanations

### L1 human

The polynomial $x$ squared plus one gives the matrix that turns the plane by a quarter turn.
Turning twice is the same as reflecting through the origin, so the square of the matrix is minus the identity.
That is the polynomial again: square plus one gives zero.
No real direction is kept by a quarter turn, so the matrix has no real eigenvalue.

### L2 human

1. Over $\mathbb{F}_5$ we have $2^2 + 1 = 5 = 0$ and $3^2 + 1 = 10 = 0$, so $2$ and $3$ are roots of $p$.
2. $C - 2I = \begin{pmatrix} -2 & -1 \\ 1 & -2 \end{pmatrix}$ has kernel spanned by $(1, 3)$, since $-2 - 3 = -5 = 0$ and $1 - 6 = -5 = 0$.
3. $C - 3I$ has kernel spanned by $(1, 2)$, since $-3 - 2 = -5 = 0$ and $1 - 6 = -5 = 0$.
4. With $P$ the matrix with columns $(1, 3)$ and $(1, 2)$, $CP = P \operatorname{diag}(2, 3)$.

The typical use is to see that a companion matrix is diagonalizable exactly when its polynomial has distinct roots in the field.
The trap is to call $C$ "not diagonalizable" without naming the field.
