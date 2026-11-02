---
tag: 88VFJSZ8X2
kind: definition
name: Gaussian curvature
msc: [53A05]
defines: SQVQ5DQT6W
uses: [6080X3FAD4, FA8QE1SGP4, DQCD11X1VM, MAJ3DH7MZS, 9KHQR16P1B, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_curvature
---

## Definition

Let $S \subseteq \R^3$ be a [[regular surface|6080X3FAD4]], let $p \in S$, and choose a smooth unit normal field near $p$.
Let $S_p$ be the [[shape operator|DQCD11X1VM]] at $p$ and let $k_1, k_2$ be the [[principal curvatures|FA8QE1SGP4]] at $p$.
The *Gaussian curvature* of $S$ at $p$ is
$$K(p) = \det S_p = k_1 k_2.$$
It does not depend on the choice of the unit normal.

## Remarks

In a local parametrisation, with $E, F, G$ the coefficients of the [[first fundamental form|MAJ3DH7MZS]] and $e, f, g$ those of the [[second fundamental form|9KHQR16P1B]],
$$K = \frac{e g - f^2}{E G - F^2}.$$
Example: on the sphere of radius $r$, $S_p = \pm \frac{1}{r} \id$, so $K = 1/r^2$.
On a cylinder $k_1 = 1/r$ and $k_2 = 0$, so $K = 0$; on the saddle $z = xy$ at the origin $k_1 = 1$ and $k_2 = -1$, so $K = -1$.
Non-example: on that saddle, the normal curvatures in the orthogonal directions $(1, 0, 0)$ and $(0, 1, 0)$ are both $0$.
Their product $0$ is not $K = -1$, because these directions are not principal directions.
For the graph $z = h(x, y)$ of a smooth function, $K = (h_{xx} h_{yy} - h_{xy}^2) / (1 + h_x^2 + h_y^2)^2$.
