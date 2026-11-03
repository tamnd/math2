---
tag: QDV9SBK6W0
kind: statement
role: fact
name: Snell's law
msc: [78A05]
uses: [9VGK0SP6EQ, RKX9XJ0RVW, 0WQJJCCTC8]
about: [9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Snell%27s_law
same_as:
  wikidata: Q208391
  wikipedia: Snell's law
---

## Statement

Let two homogeneous isotropic media with [[refractive indices|9VGK0SP6EQ]] $n_1$ and $n_2$ meet along a plane interface.
Let a ray in the first medium hit the interface and pass into the second medium.
Let $\theta_1 \in [0, \pi/2)$ be its angle with the [[normal|0WQJJCCTC8]] to the interface.
Then the refracted ray lies in the plane spanned by the incident ray and the normal, on the other side of the normal.
Its angle $\theta_2$ with the normal satisfies
$$n_1 \sin\theta_1 = n_2 \sin\theta_2.$$

## Remarks

One proof uses [[Fermat's principle|RKX9XJ0RVW]].
A ray from $A$ in the first medium to $B$ in the second crosses the interface at a point $x$, and its optical path length is $n_1 \abs{A - x} + n_2 \abs{x - B}$.
Setting the derivative in $x$ to zero gives exactly $n_1 \sin\theta_1 = n_2 \sin\theta_2$.
A wave proof matches the phases of the incident and transmitted plane waves along the interface: their wave vectors must have the same component along it.

Example: light from air ($n_1 = 1$) into water ($n_2 \approx 1.33$) at $\theta_1 = 45^\circ$ has $\sin\theta_2 \approx 0.707 / 1.33 \approx 0.53$, so $\theta_2 \approx 32^\circ$; the ray bends toward the normal.

If $n_1 > n_2$ and $\sin\theta_1 > n_2 / n_1$, no angle $\theta_2$ satisfies the law.
Then there is no refracted ray and the light is totally reflected.

## Explanations

### L1 human

A straw in a glass of water looks bent at the surface.
This is because light changes direction when it passes from water to air.
Snell's law gives the new direction: the sine of the angle times the refractive index is the same on both sides.
Light going into a slower medium bends toward the perpendicular, and light going into a faster medium bends away from it.

### L2 human

Snell's law is the basic rule for tracing rays through lenses and prisms.
In the paraxial approximation it becomes $n_1 \theta_1 = n_2 \theta_2$, which leads to the matrix methods of first-order optics.
Its critical angle gives total internal reflection, the principle of optical fibres.
In a medium with a continuously varying index stratified in layers, the quantity $n \sin\theta$ stays constant along the ray, which explains mirages.
