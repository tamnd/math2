---
tag: BW6XGX673E
kind: definition
name: Associated flow rule
msc: [74C05]
defines: 80NPDZSKBT
uses: [A3V75E17RS, CWWCEXZ8BH]
sources:
  - url: https://en.wikipedia.org/wiki/Flow_plasticity_theory
---

## Definition

Consider a [[flow plasticity model|A3V75E17RS]] with yield function $f(\sigma, q)$, differentiable in $\sigma$.
Its flow rule is *associated* if the plastic strain rate is
$$\dot\varepsilon^p = \dot\lambda \, \frac{\partial f}{\partial \sigma}(\sigma, q), \qquad \dot\lambda \ge 0,$$
that is, if the plastic potential $g$ equals $f$.

## Remarks

Then $\dot\varepsilon^p$ is an outward normal to the [[yield surface|CWWCEXZ8BH]] at $\sigma$.
At a corner of a non-smooth yield surface, such as those of the Tresca hexagon, the rule says that $\dot\varepsilon^p$ lies in the cone of outward normals at that point.
Example: for $f(\sigma) = \sqrt{3J_2} - \sigma_y$, with $s$ the deviatoric stress and $J_2 = \tfrac12 s:s$, one has $\partial f / \partial \sigma = \frac{3 s}{2 \sqrt{3 J_2}}$.
So $\dot\varepsilon^p$ is parallel to $s$, and $\tr \dot\varepsilon^p = \tr s = 0$: plastic flow does not change volume.
Non-example: for soils with the Drucker–Prager yield function, models often take a plastic potential $g \ne f$ with a smaller pressure term, to reduce the dilatancy; such a flow rule is non-associated.

## Explanations

### L1 human

The plastic strain rate is a nonnegative multiple of the gradient of the yield function.
So plastic flow is perpendicular to the yield surface.
