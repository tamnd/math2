---
tag: AQADG9N8EV
kind: statement
role: proposition
name: Haversine formula
msc: [51M09, 86A30]
uses: [5K7ZVAQM4A, SXQGHWHFRF]
about: [5K7ZVAQM4A]
sources:
  - url: https://en.wikipedia.org/wiki/Haversine_formula
same_as:
  wikidata: Q587172
  wikipedia: Haversine formula
---

## Statement

For a real number $x$, let $\operatorname{hav} x = \sin^2(x/2) = (1 - \cos x)/2$.
Let $P$ and $Q$ be points on a sphere of radius $r > 0$, with latitudes $\varphi_1, \varphi_2$ and longitudes $\lambda_1, \lambda_2$.
Let $d$ be the [[great-circle distance|5K7ZVAQM4A]] between $P$ and $Q$, and let $\theta = d/r$.
Then
$$\operatorname{hav}\theta = \operatorname{hav}(\varphi_2 - \varphi_1) + \cos\varphi_1 \cos\varphi_2 \operatorname{hav}(\lambda_2 - \lambda_1).$$
Consequently
$$d = 2r \arcsin\sqrt{\operatorname{hav}(\varphi_2 - \varphi_1) + \cos\varphi_1 \cos\varphi_2 \operatorname{hav}(\lambda_2 - \lambda_1)}.$$

## Remarks

The proof starts from the spherical law of cosines, $\cos\theta = \sin\varphi_1 \sin\varphi_2 + \cos\varphi_1 \cos\varphi_2 \cos(\lambda_2 - \lambda_1)$.
Substitute $\cos x = 1 - 2\operatorname{hav} x$ for $x = \theta$ and $x = \lambda_2 - \lambda_1$.
Then use $\cos(\varphi_2 - \varphi_1) = \cos\varphi_1\cos\varphi_2 + \sin\varphi_1\sin\varphi_2$ and rearrange.
The second formula follows because $\theta/2 \in [0, \pi/2]$, where $\sin$ is invertible.
Example: two points on the equator with $\lambda_2 - \lambda_1 = \pi/2$ give $\operatorname{hav}\theta = 1/2$, so $\theta = \pi/2$ and $d = \pi r/2$.

## Explanations

### L1 human

The formula computes the distance along the surface of a sphere from latitudes and longitudes.
It gives the same answer as the usual cosine formula, but in a form that stays accurate for nearby points.
For two cities $1$ km apart, the cosine of the angle is extremely close to $1$, and rounding destroys the answer.
The haversine of a small angle is small, so no such loss happens.

### L2 human

The haversine form is a rewriting of the spherical law of cosines from [[spherical trigonometry|SXQGHWHFRF]].
Its numerical weakness is the opposite case: for nearly antipodal points, the argument of $\arcsin$ is close to $1$.
A formula with $\operatorname{atan2}$, as used by Vincenty for the sphere, is accurate for all pairs.
On the Earth, the spherical model gives errors up to about $0.5\%$; for better accuracy one solves the [[geodesic problem on the ellipsoid|KA7Z56ZFPQ]].
