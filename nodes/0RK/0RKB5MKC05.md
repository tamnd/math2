---
tag: 0RKB5MKC05
kind: definition
name: Circumcircle
msc: [51M04]
defines: 03VZJE6C8C
uses: [0F98FZK14A, 060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Circumcircle
    locator: lead section
---

## Definition

Let $ABC$ be a triangle in the Euclidean plane $\mathbb{R}^2$, with [[circumcentre|0F98FZK14A]] $O$ and circumradius $R = d(O, A)$, where $d$ is the Euclidean distance.
The circumcircle of $ABC$ is the [[circle|060W5CBZP6]] with the centre $O$ and the radius $R$:
$$\{\, X \in \mathbb{R}^2 \;:\; d(X, O) = R \,\}.$$
It is the unique circle that contains $A$, $B$ and $C$.

## Remarks

For a triangle in $\mathbb{R}^n$, the circumcircle is the circle in the plane of the triangle with the centre $O$ and the radius $R$. Mathlib's `Affine.Simplex.circumsphere` is the sphere with this centre and radius in the ambient space.
The [[law of sines|0PASQ34GHG]] gives $2R = a / \sin \alpha$, with the side $a$ opposite the angle $\alpha$.
A polygon whose vertices all lie on one circle is a cyclic polygon. Each triangle is cyclic, but not each quadrilateral is.

## Explanations

### L1 human

Through any three points that are not on one line, there is exactly one circle. For a triangle, this is the circumcircle. For the right triangle with the vertices $(0, 0)$, $(4, 0)$ and $(0, 3)$, the circumcircle has the centre $(2, 1.5)$ and the radius $2.5$.
