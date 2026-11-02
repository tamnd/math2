---
tag: DT6WEXJANH
kind: definition
name: Spherical harmonics
msc: [33C55]
defines: 3F32Y21HP4
uses: [2C3PAQ7H50, 0DEB0JMN0W, T62369RFH6]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_harmonics
---

## Definition

Let $d \ge 2$ and $\ell \ge 0$ be integers, and let $S^{d-1} = \set{x \in \R^d : \norm{x} = 1}$ be the unit [[sphere|T62369RFH6]].
A *spherical harmonic of degree $\ell$* is a function $Y \colon S^{d-1} \to \C$ such that $Y = p|_{S^{d-1}}$ for some polynomial $p$ on $\R^d$ that is:

1. a [[homogeneous polynomial|2C3PAQ7H50]] of degree $\ell$, and
2. [[harmonic|0DEB0JMN0W]], that is, $\Delta p = \sum_{j=1}^{d} \frac{\partial^2 p}{\partial x_j^2} = 0$.

The spherical harmonics of degree $\ell$ form a complex vector space $\mathcal{H}_\ell(S^{d-1})$.

## Remarks

Example: on $S^2$, $Y(x, y, z) = x^2 - y^2$ is a spherical harmonic of degree $2$, since $\Delta(x^2 - y^2) = 2 - 2 = 0$.
Non-example: $x^2$ is homogeneous of degree $2$ but $\Delta x^2 = 2 \ne 0$.
On $S^2$ it equals $\left( x^2 - \frac13 (x^2 + y^2 + z^2) \right) + \frac13$, a sum of harmonics of degrees $2$ and $0$, so it is not a spherical harmonic of degree $2$.
For $d \ge 3$, the dimension of $\mathcal{H}_\ell(S^{d-1})$ is $\binom{\ell + d - 1}{d - 1} - \binom{\ell + d - 3}{d - 1}$, which is $2\ell + 1$ for $d = 3$; for $d = 2$ it is $2$ when $\ell \ge 1$.
Each $Y \in \mathcal{H}_\ell$ satisfies $\Delta_{S^{d-1}} Y = -\ell(\ell + d - 2) Y$ for the Laplace–Beltrami operator of the sphere.
The spaces $\mathcal{H}_\ell$ are pairwise orthogonal in $L^2(S^{d-1})$, and their sum is dense.
For $d = 3$, in spherical coordinates, a standard orthonormal basis is $Y_\ell^m(\theta, \varphi) = \sqrt{\frac{2\ell + 1}{4\pi} \frac{(\ell - m)!}{(\ell + m)!}} \, P_\ell^m(\cos \theta) \, e^{im\varphi}$ for $-\ell \le m \le \ell$, where $P_\ell^m$ are the associated Legendre polynomials.
