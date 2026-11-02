---
tag: V8ZZ7A2FMF
kind: concept
name: von Mises–Fisher distribution
msc: [62H11, "60E05"]
specializes: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Mises%E2%80%93Fisher_distribution
same_as:
  wikidata: Q7941489
  wikipedia: Von Mises–Fisher distribution
---

## Summary

The von Mises–Fisher distribution is a probability distribution on the unit [[sphere|T62369RFH6]] that is concentrated around a mean direction.
Its density is proportional to $\exp(\kappa \mu^T x)$, where $\mu$ is the mean direction and $\kappa \ge 0$ controls the concentration.
It plays the role of the normal distribution in [[directional statistics|8GZJQBPBY0]].
On the circle it is the von Mises distribution, and on the ordinary sphere it is the Fisher distribution.

## Explanations

### L1 human

Imagine arrows that mostly point north but wobble a little around it.
The von Mises–Fisher distribution is the standard model for such arrows in any dimension.
The number $\kappa$ says how tightly the arrows cluster: $\kappa = 0$ means no preferred direction at all, and large $\kappa$ means a tight bundle around $\mu$.
For large $\kappa$, the arrows near $\mu$ look like a normal distribution on the tangent plane.
