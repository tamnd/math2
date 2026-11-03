---
tag: NBJR9X1V3V
kind: definition
name: Drucker stability
msc: [74C05]
defines: 2H4NP9XZE2
uses: [K8BBMTN0KV, CWWCEXZ8BH, 8QS6QMJF5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Drucker_stability
---

## Definition

Consider a material point of an elastoplastic material in the small-strain setting, at stress $\sigma$, with [[strain|8QS6QMJF5Z]] split into elastic and plastic parts, $d\varepsilon = d\varepsilon^e + d\varepsilon^p$.
Let an outside agent slowly apply a stress increment $d\sigma$, which causes the strain increment $d\varepsilon$, and then remove it.
The material is *stable in the sense of Drucker* if for every such increment:

1. $d\sigma : d\varepsilon > 0$ whenever $d\sigma \ne 0$, that is, the agent does positive work while applying the increment;
2. $d\sigma : d\varepsilon^p \ge 0$, that is, the net work done by the agent over the cycle of applying and removing the increment is not negative.

## Remarks

Here $A : B = \sum_{i,j} A_{ij} B_{ij}$.
Take a [[plasticity|K8BBMTN0KV]] model with a smooth yield function $f$.
Drucker stability implies that the elastic domain is convex.
It also implies that $d\varepsilon^p$ is a nonnegative multiple of $\partial f / \partial \sigma$, normal to the [[yield surface|CWWCEXZ8BH]].
Example: a bar with linear hardening, Young's modulus $E > 0$ and plastic modulus $H > 0$, under uniaxial plastic loading has $d\sigma = \frac{EH}{E + H} d\varepsilon$ and $d\varepsilon^p = d\sigma / H$, so $d\sigma\,d\varepsilon > 0$ and $d\sigma\,d\varepsilon^p \ge 0$.
Non-example: a softening bar, with $d\sigma = -k\,d\varepsilon$ for some $k > 0$ during plastic loading, has $d\sigma\,d\varepsilon < 0$, so clause 1 fails.
A perfectly plastic material satisfies clause 1 only with $\ge$ in place of $>$; it is said to be stable in the weaker, limiting sense.

## Explanations

### L1 human

Adding load must cost work, and loading and unloading must not give back more work than was put in.
These two conditions single out materials that do not soften.
