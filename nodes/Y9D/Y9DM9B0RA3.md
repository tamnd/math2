---
tag: Y9DM9B0RA3
kind: statement
role: theorem
name: Girard's theorem
msc: [51M09, 51M25]
uses: [SXQGHWHFRF, SQ9RQVANMG, ESGEHKPD60, GCZ8EEDCHS]
about: [SXQGHWHFRF]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_trigonometry
---

## Statement

Let $R > 0$, and let $T$ be a spherical triangle on a sphere of radius $R$, with angles $\alpha$, $\beta$, $\gamma$.
Then the area of $T$ is
$$\operatorname{Area}(T) = R^2 (\alpha + \beta + \gamma - \pi).$$

## Remarks

The quantity $E = \alpha + \beta + \gamma - \pi$ is the *spherical excess*; the theorem shows that it is positive.
Proof idea: a lune, the region between two half great circles meeting at angle $\theta$, has area $2\theta R^2$, since it is the fraction $\theta / (2\pi)$ of the sphere of area $4\pi R^2$.
The three great circles through the sides of $T$ cut the sphere into eight triangles.
Let $T'$ be the antipodal triangle; the six lunes with angles $\alpha$, $\beta$, $\gamma$ at the vertices of $T$ and of $T'$ cover the sphere.
They cover $T$ and $T'$ three times each and every other point once, so $2(2\alpha + 2\beta + 2\gamma) R^2 = 4\pi R^2 + 4 \operatorname{Area}(T)$, which gives the formula.
Example: the octant triangle with vertices $(R, 0, 0)$, $(0, R, 0)$, $(0, 0, R)$ has three right angles, so its area is $R^2 (3\pi/2 - \pi) = \pi R^2 / 2$, one eighth of $4\pi R^2$.

## Explanations

### L1 human

On a sphere, the angles of a triangle add up to more than $180^\circ$.
Girard's theorem says that the extra amount, the excess, is exactly the area of the triangle divided by $R^2$.
So on a globe one can find the area of a triangle just by measuring its three angles.

### L2 human

The theorem is the spherical case of the [[Gauss–Bonnet theorem|ESGEHKPD60]]: the integral of the Gaussian curvature $1/R^2$ over the triangle equals the angle excess.
The hyperbolic counterpart says that a [[hyperbolic triangle|GCZ8EEDCHS]] in curvature $-1$ has area $\pi - (\alpha + \beta + \gamma)$, the defect.
Since the excess is positive and tends to $0$ for small triangles, it explains why the angle sum of a small spherical triangle is close to $\pi$.
It also shows that two spherical triangles with the same angles have the same area.
In fact such triangles are congruent, by the law of cosines for angles.
