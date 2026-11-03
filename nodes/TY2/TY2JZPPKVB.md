---
tag: TY2JZPPKVB
kind: statement
role: theorem
name: Milne-Thomson circle theorem
msc: [76B99, 76G25]
uses: [Q4DVPTBHEE, 84K7TEWZ2Z, 0NAHXR1FRH]
about: [Q4DVPTBHEE]
sources:
  - url: https://en.wikipedia.org/wiki/Milne-Thomson_circle_theorem
same_as:
  wikidata: Q6860189
  wikipedia: Milne-Thomson circle theorem
---

## Statement

Let $a > 0$ and let $f$ be the [[complex potential|Q4DVPTBHEE]] of a two-dimensional, incompressible and irrotational flow in the plane $\C$.
Assume that $f$ is holomorphic in a neighbourhood of the closed disc $\abs{z} \le a$.
Define $\bar f(z) = \overline{f(\bar z)}$ and
$$w(z) = f(z) + \bar f\left(\frac{a^2}{z}\right).$$
Then $w$ is the complex potential of a flow in the region $\abs{z} > a$ with the following properties.

1. The circle $\abs{z} = a$ is a streamline of $w$.
2. In $\abs{z} > a$, the function $w$ has the same singularities as $f$.

## Remarks

On the circle, $a^2/z = \bar z$, so $\bar f(a^2/z) = \overline{f(z)}$ and $w(z) = 2\operatorname{Re} f(z)$ is real.
Hence the stream function $\operatorname{Im} w$ vanishes on the circle.
The function $\bar f$ is [[holomorphic|0NAHXR1FRH]] wherever $f$ is holomorphic at the conjugate point.
So the singularities of $\bar f(a^2/z)$ are the image points $a^2/\bar z_0$ of the singularities $z_0$ of $f$ outside the disc.
These image points lie inside the disc.
Example: the uniform stream $f(z) = Uz$ gives $w(z) = U(z + a^2/z)$, the potential flow around a circular cylinder.
A point source at $z_0$ outside the circle produces an image source at $a^2/\bar z_0$ and a sink of the same strength at the centre.

## Explanations

### L1 human

Suppose one knows a flow in open water and then places a round post in it.
The circle theorem gives the new flow at once: add a mirror image of the old flow, reflected in the circle.
The mirror image cancels the flow through the circle, so the fluid goes around the post.

### L2 human

The theorem is the circle version of the method of images.
Combined with conformal maps such as the [[Joukowsky transform|3DJ46V21KH]], it produces [[potential flows|84K7TEWZ2Z]] past airfoils and other shapes from flows past a circle.
The forces on the cylinder can then be computed with the Blasius theorem.
