---
tag: AABCR83PXG
kind: example
name: Laplacian eigenvalues of the round sphere
msc: [58J50, 33C55]
instance_of: [B8TYKV7AA1]
uses: [P9CM4GQ2T0, F4NWZNTRMD, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_harmonics
---

## Example

Let $S^n \subset \R^{n+1}$ be the unit [[sphere|P9CM4GQ2T0]] with its round metric, $n \ge 1$, and let $\Delta = -\operatorname{div} \operatorname{grad}$ be its [[Laplace–Beltrami operator|F4NWZNTRMD]].
Its eigenvalues are
$$\lambda_k = k(k + n - 1), \quad k = 0, 1, 2, \ldots.$$
The $\lambda_k$-eigenspace consists of the restrictions to $S^n$ of the homogeneous harmonic polynomials of degree $k$ on $\R^{n+1}$, the [[spherical harmonics|3F32Y21HP4]] of degree $k$.
Its dimension is
$$\binom{n + k}{n} - \binom{n + k - 2}{n},$$
with the convention that the second term is $0$ when $k < 2$.

Check of the eigenvalue: write a homogeneous harmonic polynomial of degree $k$ as $P = r^k Y$ with $r = \abs{x}$ and $Y$ a function on $S^n$.
In polar coordinates the Euclidean Laplacian is $\partial_r^2 + \frac{n}{r} \partial_r - \frac{1}{r^2} \Delta$.
Applied to $P$ it gives $r^{k-2} \big( k(k-1) + nk \big) Y - r^{k-2} \Delta Y = 0$, so $\Delta Y = k(k + n - 1) Y$.
These eigenfunctions span a dense subspace of $L^2(S^n)$, so there are no other eigenvalues.

For $S^2$ the eigenvalues are $k(k+1)$ with multiplicity $2k + 1$.
For $k = 1$ the eigenfunctions are the restrictions of the coordinate functions $x_1, \ldots, x_{n+1}$, with eigenvalue $n$.

## Remarks

Since the unit sphere has Ricci curvature $(n - 1)$ times the metric, the first nonzero eigenvalue $n$ shows that the bound in the [[Lichnerowicz–Obata theorem|TK1PT9FDV0]] is attained.
The multiplicities grow like a constant times $k^{n-1}$, which agrees with [[Weyl's law|2JK9YMZV2B]].

## Explanations

### L1 human

The sphere vibrates only at a discrete list of frequencies, and the list can be written down exactly.
The $k$-th frequency comes from polynomials of degree $k$, such as $x$ for $k = 1$ or $xy$ for $k = 2$.
On the ordinary sphere $S^2$ the values are $0, 2, 6, 12, \ldots$, with $1, 3, 5, 7, \ldots$ independent vibration patterns.
These patterns are the spherical harmonics used for orbitals in chemistry and for maps of the Earth's gravity.
