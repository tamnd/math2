---
tag: ~5bfc9fed
kind: example
name: A hyperbolic pair for the sum of two squares over the field with five elements
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
instance_of: [~70f96526, ~0d389e21]
illustrates: [~c9505cce]
uses: [~c9505cce, 0SPYAGE7T0, 0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: Hyperbolic plane
---

## Example

On $V = \mathbb{F}_5^2$ let $B(x, y) = x_1 y_1 + x_2 y_2$, with the identity matrix $I$.
All computations are modulo $5$.

1. $2^2 = 4 = -1$, so $u = (1, 2)$ has $B(u, u) = 1 + 4 = 5 = 0$. So $u$ is isotropic.
2. We follow the [[proof of the statement|~c9505cce]]. Take $z = e_1$. Then $B(u, z) = 1$ and $B(z, z) = 1$.
3. In $\mathbb{F}_5$, $\frac12 = 3$, since $2 \cdot 3 = 6 = 1$.
4. So $v = z - \frac{B(z, z)}{2} u = e_1 - 3(1, 2) = (-2, -6) = (3, 4)$.
5. A check: $B(v, v) = 9 + 16 = 25 = 0$ and $B(u, v) = 3 + 8 = 11 = 1$.
6. Let $P = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$, with the columns $u$ and $v$. Then $P^T I P = \begin{pmatrix} 5 & 11 \\ 11 & 25 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
7. So $(u, v)$ is a hyperbolic pair, and $B$ is a hyperbolic plane.

## Remarks

The two isotropic lines are spanned by $(1, 2)$ and by $(1, 3)$; note that $(3, 4) = 3 \cdot (1, 3)$.
By the [[change of basis rule|0SPYAGE7T0]], $\det(P^T I P) = (\det P)^2 \det I$.
Here $\det P = 4 - 6 = -2 = 3$, and $3^2 = 9 = 4 = -1$, which agrees with $\det \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = -1$.
Over $\mathbb{F}_3$, the same formula gives an [[anisotropic form|~d1d59548]], since $-1$ is a square modulo $5$ but not modulo $3$.

## Explanations

### L1 human

Over the field with five elements, $1 + 4 = 0$.
So the vector $(1, 2)$ gives $0$ with itself under the dot product.
We find a second such vector, $(3, 4)$, that gives $1$ with the first one.
In the basis of these two vectors, the dot product has the matrix with $0$ on the diagonal and $1$ off the diagonal.

### L2 human

The recipe to find a hyperbolic pair is the following.

1. Find an isotropic vector $u$.
2. Find $z$ with $B(u, z) = 1$.
3. Put $v = z - \frac{B(z, z)}{2} u$, and check $B(v, v) = 0$.

The typical use is to split off hyperbolic planes, one after another.
A trap: in $\mathbb{F}_5$, $\frac12$ is $3$, not $0.5$; compute inverses in the field.
