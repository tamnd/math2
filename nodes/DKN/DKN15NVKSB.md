---
tag: DKN15NVKSB
kind: concept
name: Cahn–Hilliard equation
msc: [35K55, 35K25]
sources:
  - url: https://en.wikipedia.org/wiki/Cahn%E2%80%93Hilliard_equation
same_as:
  wikidata: Q5017440
  wikipedia: Cahn–Hilliard equation
---

## Summary

The Cahn–Hilliard equation is the fourth-order parabolic equation $c_t = \Delta(c^3 - c - \gamma \Delta c)$.
It describes how a mixture of two substances separates into regions rich in one or the other.
Unlike the [[Allen–Cahn equation|7S813PEV69]], it conserves the total amount $\int c\,dx$.
It is the gradient flow of the Ginzburg–Landau energy in the $H^{-1}$ metric.

## Explanations

### L1 human

Shake oil and vinegar together, then let the mixture rest: droplets form and slowly grow.
The Cahn–Hilliard equation models this.
The concentration $c$ is near $+1$ in one substance and near $-1$ in the other.
Matter is only moved around, never created, so the average of $c$ stays fixed while the pattern coarsens.
