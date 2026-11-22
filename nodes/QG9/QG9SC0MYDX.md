---
tag: QG9SC0MYDX
kind: example
name: A hyperbolic pair for the sum of two squares over the field with five elements
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
instance_of: [1X5PZSK44P, MZHFGPV1YT]
illustrates: [SN50886T80]
uses: [SN50886T80, 0SPYAGE7T0, 0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: Hyperbolic plane
---

## Example

On $V = \mathbb{F}_5^2$ let $B$ be the [[symmetric bilinear form|0744CN4MDA]]
$$B(x, y) = x_1 y_1 + x_2 y_2,$$
whose matrix is the identity $I$.
We find an [[isotropic vector|MZHFGPV1YT]] and a partner for it, and so show that $B$ is a [[hyperbolic plane|1X5PZSK44P]].
All arithmetic is modulo $5$.

1. Since $2^2 = 4 = -1$, the vector $u = (1, 2)$ has $B(u, u) = 1 + 4 = 5 = 0$. So $u$ is isotropic.
2. We follow the [[statement on isotropic vectors|SN50886T80]]. Take $z = e_1$, which has $B(u, z) = 1$ and $B(z, z) = 1$.
3. In $\mathbb{F}_5$ we have $\tfrac{1}{2} = 3$, since $2 \cdot 3 = 6 = 1$.
4. So the corrected vector is $v = z - \tfrac{1}{2} B(z, z)\, u = (1, 0) - 3(1, 2) = (-2, -6) = (3, 4)$.
5. Check: $B(v, v) = 9 + 16 = 25 = 0$ and $B(u, v) = 3 + 8 = 11 = 1$.

Put $u$ and $v$ as the columns of $P$ and compute the new matrix:
$$P = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}, \qquad P^{\mathsf{T}} I P = \begin{pmatrix} 1 \cdot 1 + 2 \cdot 2 & 1 \cdot 3 + 2 \cdot 4 \\ 3 \cdot 1 + 4 \cdot 2 & 3 \cdot 3 + 4 \cdot 4 \end{pmatrix} = \begin{pmatrix} 5 & 11 \\ 11 & 25 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
So $(u, v)$ is a hyperbolic pair, and $B$ is a hyperbolic plane over $\mathbb{F}_5$.

## Remarks

The plane has exactly two isotropic lines.
One is spanned by $(1, 2)$, and the other by $(1, 3)$, since $1 + 9 = 10 = 0$.
The partner $v = (3, 4)$ lies on the second line, because $3 \cdot (1, 3) = (3, 9) = (3, 4)$.

The determinant gives a quick check.
By the [[change of basis rule|0SPYAGE7T0]], $\det(P^{\mathsf{T}} I P) = (\det P)^2 \det I$.
Here $\det P = 4 - 6 = -2 = 3$, and $3^2 = 9 = 4 = -1$, which agrees with $\det \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = -1$.

The field matters.
Over $\mathbb{F}_3$ the same formula is [[anisotropic|DH7M9YDXSS]], because $-1$ is a square modulo $5$ but not modulo $3$.
Over $\mathbb{F}_p$ for an odd prime $p$, the sum of two squares is a hyperbolic plane exactly when $p \equiv 1 \pmod 4$.

## Explanations

### L1 human

In the field with five elements, $1 + 4 = 5 = 0$.
So the vector $(1, 2)$ pairs to $0$ with itself under the dot product, because $1 \cdot 1 + 2 \cdot 2 = 0$ there.
A second vector, $(3, 4)$, also pairs to $0$ with itself, and it pairs to $1$ with $(1, 2)$.
In the basis made of these two vectors, the dot product has $0$ on the diagonal and $1$ off the diagonal.

### L2 human

The method above finds a hyperbolic pair in three moves.
First find an isotropic vector $u$, here by noticing that $-1$ is the square of $2$.
Then find $z$ with $B(u, z) = 1$, here $z = e_1$.
Last, put $v = z - \tfrac{1}{2} B(z, z)\, u$ and check that $B(v, v) = 0$.
Repeating these moves splits a larger space into hyperbolic planes, one at a time.
Watch out: in $\mathbb{F}_5$ the number $\tfrac{1}{2}$ is $3$, not $0.5$, so compute every inverse in the field.
