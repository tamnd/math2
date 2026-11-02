---
tag: NVRR2TXQSE
kind: statement
role: theorem
name: Addition theorem for spherical harmonics
msc: [33C55, 43A90]
uses: [3F32Y21HP4, 5TRFA6F79B, QFYGJVA996, Q5D54R3RGE, 0S9GGTR0EX]
about: [3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_harmonics
---

## Statement

Let $d \ge 3$ and $\ell \ge 0$ be integers.
Let $\mathcal{H}_\ell$ be the space of [[spherical harmonics|3F32Y21HP4]] of degree $\ell$ on the unit sphere $S^{d-1} \subset \R^d$, with dimension $N$.
Let $\sigma$ be the surface measure, $\omega = \sigma(S^{d-1})$, and $\lambda = \frac{d - 2}{2}$.
Let $Y_1, \dots, Y_N$ be an [[orthonormal basis|0S9GGTR0EX]] of $\mathcal{H}_\ell$ for the inner product $\ip{f, g} = \int_{S^{d-1}} f \, \overline{g} \, d\sigma$.
Then for all $x, y \in S^{d-1}$,
$$\sum_{j=1}^{N} Y_j(x) \, \overline{Y_j(y)} = \frac{N}{\omega} \, \frac{C_\ell^{(\lambda)}(x \cdot y)}{C_\ell^{(\lambda)}(1)},$$
where $C_\ell^{(\lambda)}$ is the [[Gegenbauer polynomial|5TRFA6F79B]].
In particular, for $d = 3$ and the standard basis $Y_\ell^m$, $-\ell \le m \le \ell$,
$$P_\ell(x \cdot y) = \frac{4\pi}{2\ell + 1} \sum_{m=-\ell}^{\ell} Y_\ell^m(x) \, \overline{Y_\ell^m(y)},$$
where $P_\ell$ is the [[Legendre polynomial|QFYGJVA996]].

## Remarks

Proof idea: the left side $K(x, y)$ is the [[zonal spherical harmonic|Q5D54R3RGE]] $Z_y^{(\ell)}(x)$, so it does not depend on the choice of basis.
Since rotations act unitarily on $\mathcal{H}_\ell$, $K(gx, gy) = K(x, y)$ for every rotation $g$, so $K$ depends only on $x \cdot y$.
A harmonic of degree $\ell$ invariant under the rotations fixing $y$ is a multiple of $C_\ell^{(\lambda)}(x \cdot y)$.
The constant comes from $K(x, x)$ being constant and $\int_{S^{d-1}} K(x, x) \, d\sigma(x) = \sum_j \norm{Y_j}^2 = N$, so $K(x, x) = N / \omega$.
Example: for $d = 3$ and $\ell = 1$, the basis $\sqrt{3/(4\pi)} \, x_i$, $i = 1, 2, 3$, gives $\frac{3}{4\pi} \, x \cdot y = \frac{3}{4\pi} P_1(x \cdot y)$.
Setting $x = y$ gives Unsöld's theorem: $\sum_{m=-\ell}^{\ell} \abs{Y_\ell^m(x)}^2 = \frac{2\ell + 1}{4\pi}$ at every point of $S^2$.

## Explanations

### L1 human

Pick two points on a sphere.
Summing the products of all basic patterns of degree $\ell$ at the two points gives a number that depends only on the angle between the points.
That number is a Legendre polynomial of the cosine of the angle, up to a fixed factor.
So a complicated sum over many functions collapses to a single simple function.

### L2 human

The theorem identifies the reproducing kernel of $\mathcal{H}_\ell$ with a Gegenbauer polynomial in $x \cdot y$.
It gives the projection of a function $f$ onto $\mathcal{H}_\ell$ as the convolution $\frac{N}{\omega} \int_{S^{d-1}} f(y) \frac{C_\ell^{(\lambda)}(x \cdot y)}{C_\ell^{(\lambda)}(1)} \, d\sigma(y)$.
Combined with the generating function of the Legendre polynomials, it expands $1/\norm{x - y}$ in spherical harmonics, the standard multipole expansion of potential theory.
It also gives the bound $\abs{Y(x)} \le \sqrt{N / \omega} \, \norm{Y}_{L^2}$ for every $Y \in \mathcal{H}_\ell$.
