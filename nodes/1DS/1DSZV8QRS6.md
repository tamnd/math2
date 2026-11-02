---
tag: 1DSZV8QRS6
kind: definition
name: Translation surface
msc: ["37E35", "30F30", "32G15"]
defines: CEHHBBD6NT
uses: [5K0N8QMV6Q, P014C13K5H, NJ787GZS1N, 03NM7DZXXC]
sources:
  - url: https://en.wikipedia.org/wiki/Translation_surface
---

## Definition

A *translation surface* is a pair $(X, \omega)$ with the following data.
$X$ is a compact connected [[Riemann surface|5K0N8QMV6Q]].
$\omega$ is a holomorphic 1-form on $X$, an [[abelian differential|P014C13K5H]], that is not identically zero.
Two translation surfaces $(X, \omega)$ and $(X', \omega')$ are the same if there is a biholomorphic map $\phi \colon X \to X'$ with $\phi^* \omega' = \omega$.

## Remarks

Let $\Sigma$ be the finite set of zeros of $\omega$.
Near a point $p \notin \Sigma$, the function $z(q) = \int_p^q \omega$ is a local coordinate in which $\omega = dz$, and two such coordinates differ by a translation $z \mapsto z + c$.
So $X \setminus \Sigma$ gets a flat metric $\abs{\omega}$, and a zero of order $k$ is a cone point of angle $2\pi(k + 1)$.
If $X$ has [[genus|NJ787GZS1N]] $g$ and the zeros have orders $k_1, \dots, k_n$, then $k_1 + \cdots + k_n = 2g - 2$.

Equivalently, a translation surface is given by finitely many polygons in $\C$ whose sides are glued in pairs by translations.
Each side is glued to a parallel side of the same length with opposite outward normal.
The form $\omega$ is $dz$ on each polygon.

Example: the unit square with opposite sides glued is the [[torus|03NM7DZXXC]] $X = \C / (\Z + i\Z)$ with $\omega = dz$.
The form $dz$ is invariant under the translations by $\Z + i \Z$, so it descends to $X$, and it has no zeros, in line with $2g - 2 = 0$.

Example: the regular octagon with opposite sides glued has all eight vertices glued to one point, with total angle $8 \cdot \frac{3\pi}{4} = 6\pi$.
So $\omega$ has one zero of order $2$, and $2 = 2g - 2$ gives genus $g = 2$.

Non-example: $(X, 0)$ is not a translation surface, since the zero form gives no charts.
