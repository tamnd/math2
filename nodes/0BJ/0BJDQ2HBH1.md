---
tag: 0BJDQ2HBH1
kind: definition
name: Tangent plane and normal vector of a surface
msc: [53A05]
defines: 073JKP99K2
uses: [05788J51WZ, 05AXG3QRKR, 0NS2QYVC4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Parametric_surface
    locator: Tangent plane and normal vector
  - url: https://en.wikipedia.org/wiki/Normal_(geometry)
    locator: Normal to general surfaces in 3D space
  - url: https://en.wikipedia.org/wiki/Normal_(geometry)
    locator: Orientation
---

## Definition

Let $r \colon D \to \mathbb{R}^3$ be a [[parametrised surface|05788J51WZ]] that is regular at the point $(u_0, v_0)$ of $D$, and let $p = r(u_0, v_0)$.
The tangent plane at $p$ is the plane $\{ p + s \, r_u(u_0, v_0) + t \, r_v(u_0, v_0) : s, t \in \mathbb{R} \}$.
The vector $N(u_0, v_0) = r_u(u_0, v_0) \times r_v(u_0, v_0)$ is the normal vector of $r$ at $(u_0, v_0)$, and $n = N / \|N\|$ is the unit normal vector.

## Remarks

The vector $N$ is perpendicular to $r_u$ and $r_v$, so it is perpendicular to the tangent plane. The other unit normal at $p$ is $-n$.
For the graph $z = f(x, y)$, the normal is $(-f_x, -f_y, 1)$, which points upward.
If the surface is the level set $g(x, y, z) = c$ of a $C^1$ function $g$ with $\nabla g(p) \ne 0$, then the [[gradient|0NS2QYVC4Y]] $\nabla g(p)$ is a normal vector at $p$.
For the unit sphere with $r(\varphi, \theta) = (\sin \varphi \cos \theta, \sin \varphi \sin \theta, \cos \varphi)$, one gets $r_\varphi \times r_\theta = \sin \varphi \, r(\varphi, \theta)$, which points outward for $0 < \varphi < \pi$.

## Explanations

### L1 human

The tangent plane is the flat plane that touches the surface at a point, and the normal vector sticks straight out of it.
The cross product of the two coordinate tangent vectors gives a normal at once.
