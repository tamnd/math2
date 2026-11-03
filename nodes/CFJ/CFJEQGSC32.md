---
tag: CFJEQGSC32
kind: definition
name: Fresnel's wave surface
msc: [78A10, 78A05]
defines: 9ZXST6JR11
uses: [8CWCYQJ44T, NRF1ESCGMR, F768YN0P2V]
sources:
  - url: https://en.wikipedia.org/wiki/Birefringence
---

## Definition

Let a linear, non-magnetic, transparent medium have relative [[permittivity|F768YN0P2V]] tensor $\mathrm{diag}(\varepsilon_x, \varepsilon_y, \varepsilon_z)$ in principal axes, with all $\varepsilon_j > 0$.
Let $c$ be the speed of light in vacuum and let $v_j = c / \sqrt{\varepsilon_j}$ be the *principal speeds*.
Write $r^2 = x^2 + y^2 + z^2$.
*Fresnel's wave surface* of the medium is the set of points $(x, y, z) \in \R^3$ such that
$$r^2 \left(v_x^2 x^2 + v_y^2 y^2 + v_z^2 z^2\right) - v_x^2 (v_y^2 + v_z^2) x^2 - v_y^2 (v_x^2 + v_z^2) y^2 - v_z^2 (v_x^2 + v_y^2) z^2 + v_x^2 v_y^2 v_z^2 = 0.$$

## Remarks

Away from the coordinate spheres $r = v_j$, the equation is equivalent to Fresnel's form $\sum_j v_j^2 x_j^2 / (r^2 - v_j^2) = 0$.
Take the point at distance $r$ from the origin in a direction $\mathbf{t}$.
It lies on the surface exactly when $r$ is the ray speed of one of the two modes whose energy flows along $\mathbf{t}$.
So the surface is the wavefront at time $1$ of a point source at the origin.

Example: in a uniaxial medium with $v_x = v_y = v_o$ and $v_z = v_e$, the left side factors as
$$\left(r^2 - v_o^2\right)\left(v_o^2 (x^2 + y^2) + v_e^2 z^2 - v_o^2 v_e^2\right).$$
So the surface is the sphere of radius $v_o$, the ordinary wave, together with the spheroid $(x^2 + y^2)/v_e^2 + z^2/v_o^2 = 1$, the extraordinary wave.
The two sheets touch at the two points $(0, 0, \pm v_o)$ on the optic axis.

Non-example: in an isotropic medium with all $v_j = v$, the left side becomes $v^2 (r^2 - v^2)^2$, so the equation is $(r^2 - v^2)^2 = 0$.
This is a doubly counted sphere, and the medium is not [[birefringent|8CWCYQJ44T]].

In a biaxial medium with distinct $v_j$, the two sheets meet in four conical points that lie on the two optic ray axes.
The wave surface is dual to the surface of wave normals built from the [[index ellipsoid|NRF1ESCGMR]].
