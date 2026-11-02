---
tag: CBT8F8S8JT
kind: problem
name: Euler's elastica
msc: [49K05, 74K10, 53A04]
uses: [7JQS6VKFEZ, EWS4WFTA7W, 6FY0KHMK5A, 0SHPXM2HWH, FF9ZPCZ59K]
about: [7JQS6VKFEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Elastica_theory
history:
  posed_by: "Jacob Bernoulli"
  first_stated: "1691"
---

## Problem

Let $\ell > 0$.
Consider plane curves $\gamma \colon [0, \ell] \to \R^2$ of class $C^2$, parametrised by arc length.
Prescribe the end points $\gamma(0)$, $\gamma(\ell)$ and the unit tangents $\gamma'(0)$, $\gamma'(\ell)$.
Among such curves, find those that make the bending energy
$$E(\gamma) = \frac{1}{2} \int_0^\ell \kappa(s)^2 \, ds$$
stationary, where $\kappa$ is the signed [[curvature|7JQS6VKFEZ]] of $\gamma$.
The solutions are the *elasticae*, the shapes of a thin elastic rod held at its ends.

## Remarks

Write $\gamma'(s) = (\cos \theta(s), \sin \theta(s))$, so that $\kappa = \theta'$.
Let $(X, Y) = \gamma(\ell) - \gamma(0)$.
The end points give the constraints $\int_0^\ell \cos \theta \, ds = X$ and $\int_0^\ell \sin \theta \, ds = Y$.
So this is an [[isoperimetric problem|6FY0KHMK5A]] with two constraints.
With multipliers, the Euler–Lagrange equation becomes
$$\theta'' + c \sin(\theta - \theta_0) = 0$$
for constants $c$ and $\theta_0$, the equation of a [[pendulum|0SHPXM2HWH]].
So the solutions are expressed through elliptic integrals and [[elliptic functions|FF9ZPCZ59K]].
Euler classified the possible shapes of the elasticae in 1744.

## Explanations

### L1 human

Bend a thin flexible ruler or a steel wire and hold its two ends.
It takes the shape that stores the least bending energy, which is measured by how sharply it curves along its length.
The angle of the wire along its length obeys the same equation as a swinging pendulum, and this gives a whole family of shapes, from gentle arcs to loops.
