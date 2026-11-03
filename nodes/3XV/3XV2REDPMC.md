---
tag: 3XV2REDPMC
kind: definition
name: Index ellipsoid
msc: [78A10, 78A05]
defines: NRF1ESCGMR
uses: [F768YN0P2V, 9VGK0SP6EQ, Q3Q4FF23VG, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Index_ellipsoid
---

## Definition

Let a linear, non-magnetic, transparent medium have relative [[permittivity|F768YN0P2V]] tensor $\varepsilon$, a real symmetric [[positive definite|0KX66CZMBB]] $3 \times 3$ matrix.
The *index ellipsoid* of the medium is the [[quadric|Q3Q4FF23VG]]
$$\set{\mathbf{r} \in \R^3 : \mathbf{r}^T \varepsilon^{-1} \mathbf{r} = 1}.$$
In principal axes, where $\varepsilon = \mathrm{diag}(n_x^2, n_y^2, n_z^2)$, its equation is
$$\frac{x^2}{n_x^2} + \frac{y^2}{n_y^2} + \frac{z^2}{n_z^2} = 1,$$
so its semi-axes are the principal [[refractive indices|9VGK0SP6EQ]] $n_x, n_y, n_z$.

## Remarks

For a unit vector $\mathbf{s}$, the plane through the origin orthogonal to $\mathbf{s}$ cuts the ellipsoid in an ellipse.
The lengths of its semi-axes are the refractive indices of the two plane waves with wave normal $\mathbf{s}$, and the axes give the directions of their $\mathbf{D}$ fields.

Example: for $\varepsilon = \mathrm{diag}(n_o^2, n_o^2, n_e^2)$ the index ellipsoid is a spheroid about the $z$-axis.
The plane orthogonal to $z$ cuts it in a circle of radius $n_o$, so light along $z$ has one index.
The plane orthogonal to $x$ cuts it in an ellipse with semi-axes $n_o$ along $y$ and $n_e$ along $z$.

Non-example: if $\varepsilon$ has one or two negative eigenvalues, as in some artificial media, the quadric $\mathbf{r}^T \varepsilon^{-1} \mathbf{r} = 1$ is a hyperboloid, not an ellipsoid.
The construction needs $\varepsilon$ to be positive definite.

A general biaxial ellipsoid has exactly two central circular sections; the normals to them are the two optic axes.
