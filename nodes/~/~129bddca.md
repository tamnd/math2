---
tag: ~129bddca
kind: concept
name: Work done by a force field
aliases: [work-of-a-force]
msc: [26B12]
uses: [~3928c498, ~edfef10c]
sources:
  - url: https://en.wikipedia.org/wiki/Work_(physics)
    locator: Work done by a variable force
  - url: https://en.wikipedia.org/wiki/Work_(physics)
    locator: Mathematical calculation
---

## Summary

The work done by a force field $F$ on a particle that moves along a curve $\gamma$ is the [[line integral|~3928c498]] $W = \int_\gamma F \cdot d\mathbf{r}$.
Only the component of the force along the direction of motion contributes, positively when it points forward and negatively when it points backward.

## Remarks

For a constant force $F$ and a straight displacement $d$, the work is $F \cdot d$.
For a $C^1$ path, $W = \int_a^b F(\gamma(t)) \cdot \gamma'(t) \, dt$. The integrand $F \cdot \gamma'$ is the power, the rate at which the force does work.
If $F = -\nabla U$ for a potential energy $U$, then $W = U(\gamma(a)) - U(\gamma(b))$, and the work does not depend on the path. Gravity near the surface of the Earth is an example.
A force that is always orthogonal to the velocity does no work.

## Explanations

### L1 human

Work measures how much a force helps a motion.
Pushing a box forward does positive work, pushing against its motion does negative work, and pushing straight down on a sliding box does no work.
