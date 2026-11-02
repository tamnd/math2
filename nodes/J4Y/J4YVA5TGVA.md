---
tag: J4YVA5TGVA
kind: definition
name: Zonal spherical harmonics
msc: [33C55, 43A90]
defines: Q5D54R3RGE
uses: [3F32Y21HP4, 0NB0AWGJBW]
sources:
  - url: https://en.wikipedia.org/wiki/Zonal_spherical_harmonics
---

## Definition

Let $d \ge 2$ and $\ell \ge 0$ be integers, and let $\sigma$ be the surface measure on the unit sphere $S^{d-1} \subset \R^d$.
Let $\mathcal{H}_\ell$ be the space of [[spherical harmonics|3F32Y21HP4]] of degree $\ell$ on $S^{d-1}$.
Equip $\mathcal{H}_\ell$ with the [[inner product|0NB0AWGJBW]] $\ip{f, g} = \int_{S^{d-1}} f \, \overline{g} \, d\sigma$.
Let $y \in S^{d-1}$.
The *zonal spherical harmonic* of degree $\ell$ with pole $y$ is the unique $Z_y^{(\ell)} \in \mathcal{H}_\ell$ such that
$$Y(y) = \int_{S^{d-1}} Y(x) \, \overline{Z_y^{(\ell)}(x)} \, d\sigma(x) \quad \text{for all } Y \in \mathcal{H}_\ell.$$

## Remarks

It exists and is unique because $Y \mapsto Y(y)$ is a linear functional on the finite-dimensional inner product space $\mathcal{H}_\ell$.
If $Y_1, \dots, Y_N$ is an orthonormal basis of $\mathcal{H}_\ell$, then $Z_y^{(\ell)}(x) = \sum_{j=1}^{N} Y_j(x) \overline{Y_j(y)}$.
It is real-valued, and $Z_{gy}^{(\ell)}(gx) = Z_y^{(\ell)}(x)$ for every rotation $g$, so it depends only on $x \cdot y$.
Example: for $d = 3$ and $\ell = 1$, $Z_y^{(1)}(x) = \frac{3}{4\pi} \, x \cdot y$.
Check: every $Y \in \mathcal{H}_1$ has the form $Y(x) = x \cdot a$ with $a \in \C^3$, and $\int_{S^2} (x \cdot a)(x \cdot y) \, d\sigma(x) = \frac{4\pi}{3} \, a \cdot y$, so the integral returns $a \cdot y = Y(y)$.
Non-example: the function $x \mapsto x \cdot y$ itself is zonal and lies in $\mathcal{H}_1$, but it fails the reproducing identity, since it returns $\frac{4\pi}{3} Y(y)$ instead of $Y(y)$.
In general $Z_y^{(\ell)}(x) = \frac{N}{\sigma(S^{d-1})} \frac{C_\ell^{(\lambda)}(x \cdot y)}{C_\ell^{(\lambda)}(1)}$ for $d \ge 3$, with $\lambda = \frac{d - 2}{2}$, $N = \dim \mathcal{H}_\ell$ and $C_\ell^{(\lambda)}$ the [[Gegenbauer polynomial|5TRFA6F79B]].
